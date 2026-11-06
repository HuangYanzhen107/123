import {cpSync,mkdirSync,rmSync,existsSync} from 'node:fs';
// Explicit publish surface. Source documents and future PDF inputs stay private.
rmSync('dist',{recursive:true,force:true});mkdirSync('dist');
for(const entry of ['index.html','404.html','robots.txt','_headers','_redirects','assets','collections','pages','products']){
 if(!existsSync(entry))throw new Error('Missing publish entry: '+entry);
 cpSync(entry,'dist/'+entry,{recursive:true});
}
console.log('Built jewellery-only static site in dist/');
