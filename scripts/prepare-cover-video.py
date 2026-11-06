#!/usr/bin/env python3
"""Build silent seamless campaign loops from user-supplied source clips.

Uses cosine-eased forward/reverse original-frame selection. No optical-flow,
face, hand or jewellery interpolation. Raw input files are never published.
Requires local ffmpeg and numpy; not needed by the normal site build.
"""
import argparse,hashlib,json,math,subprocess
from pathlib import Path
import numpy as np

def run(args):
    return subprocess.run(args,capture_output=True,check=True).stdout

def loop(src,dest,seconds,fps=24,crf=20,preset='slow',width=None):
    meta=json.loads(run(['ffprobe','-v','quiet','-select_streams','v:0','-show_entries','stream=width,height','-of','json',str(src)]))['streams'][0]
    w,h=meta['width'],meta['height']
    resize=[]
    if width:
        w,h=width,2*round(width*h/w/2)
        resize=['-vf',f'scale={w}:{h}']
    raw=run(['ffmpeg','-v','error','-i',str(src),*resize,'-an','-f','rawvideo','-pix_fmt','rgb24','-'])
    frames=np.frombuffer(raw,dtype=np.uint8).reshape(-1,h,w,3)
    count=round(seconds*fps)
    indices=[round((1-math.cos(2*math.pi*i/count))*.5*(len(frames)-1)) for i in range(count)]
    p=subprocess.Popen(['ffmpeg','-y','-v','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{w}x{h}','-r',str(fps),'-i','-','-an','-c:v','libx264','-threads','4','-preset',preset,'-crf',str(crf),'-pix_fmt','yuv420p','-movflags','+faststart',str(dest)],stdin=subprocess.PIPE)
    for i in indices:p.stdin.write(frames[i].tobytes())
    p.stdin.close()
    if p.wait():raise RuntimeError('Encoding failed')
    return {'source':src.name,'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'seconds':seconds,'source_frames':len(frames),'output_frames':count,'seam_source_indices':[indices[-1],indices[0]],'file':dest.name}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--sources',type=Path,required=True)
    scope=parser.add_mutually_exclusive_group()
    scope.add_argument('--rings-only',action='store_true')
    scope.add_argument('--campaign-only',action='store_true')
    args=parser.parse_args()
    root=Path(__file__).resolve().parent.parent;out=root/'assets/campaign';out.mkdir(exist_ok=True);report=[]
    if not args.rings_only:
        model=args.sources/'nova-well-cover-8s-silver-v3-optimized-2k-30fps-silent.mp4'
        earrings=args.sources/'cover-video-earring-v1.mp4'
        desktop=out/'model-loop-desktop.mp4'
        mobile=out/'model-loop-mobile.mp4'
        earring_film=out/'earring-loop.mp4'
        report.append(loop(model,desktop,16,fps=30,crf=21,preset='fast'))
        run(['ffmpeg','-y','-v','error','-i',str(desktop),'-vf','crop=1080:1440:1232:0,scale=720:960','-an','-c:v','libx264','-threads','4','-preset','medium','-crf','22','-pix_fmt','yuv420p','-movflags','+faststart',str(mobile)])
        report.append(loop(earrings,earring_film,20,crf=23,preset='medium',width=800))
        for film,poster,scale in [(desktop,'model-poster-desktop.webp','1600:-2'),(mobile,'model-poster-mobile.webp','720:-2'),(earring_film,'earring-poster.webp','800:-2')]:
            run(['ffmpeg','-y','-v','error','-i',str(film),'-vf','scale='+scale,'-frames:v','1','-c:v','libwebp','-quality','85',str(out/poster)])
    if not args.campaign_only:
        for tone,name in [('gold','f7acf270b264b3407895a64fabf27415.mp4'),('silver','496ae3e6cbb8c9e6286d338b3ed3e205.mp4')]:
            report.append(loop(args.sources/name,out/f'ring-{tone}-loop.mp4',8))
    print(json.dumps(report,indent=2))
if __name__=='__main__':main()
