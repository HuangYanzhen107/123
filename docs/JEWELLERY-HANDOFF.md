# NOVA WELL 纯首饰主题交接

更新：2026-11-05。本文件为当前有效方向；早期多类目／彩色配饰方案仅为历史记录。

## 已确认并实现

- 品牌继续使用 NOVA WELL；重新设计为现代无衬线文字标志、字距与字体层级。
- 暖白、石灰灰、深炭色主题，移除粉／黄／蓝／绿彩色卡片。借鉴首饰站清晰目录和编辑式留白的组织方式，未复制参考品牌商标、图片或营销文案。
- 唯一主营为首饰，包含项链、手链、戒指、耳环、吊坠五个分类。三份用户PDF已导入469个型号、703条目录记录：手链181款、戒指106款、耳环182款。项链和吊坠暂无资料，保留空分类。
- 旧商品数据、旧产品HTML、旧图片、旧非首饰分类、按摩器指南、本机旧编辑器、旧商品脚本及样式从本版本中移除。旧商品地址由404页承接，未伪装成仍在售；历史Git提交仍可用于回滚。
- 旧目录通用入口 `/collections/accessories/` 跳转首饰总页；旧品牌故事入口跳转新品牌理念。五个新分类使用稳定英文路径。
- 语言为英文／简体中文，保留本机语言和地区选择。切换至纯首饰目录后，清除旧购物袋、旧编辑草稿及旧最近浏览；购物袋为空，无结算入口。
- 首屏现为用户提供的原创AI模特视频：酒红爱心耳环与银色戒指同框，单独制作手机裁切；保留可见的AI概念影像／非商品实拍说明。戒指区支持金银切换，造型细节弹层使用用户商品参考图。它们不作为PDF商品实拍或已确认可售SKU。详见 HOME-COVER-HANDOFF.md。
- 保留搜索、购物袋、地区设置、尺寸指南、材质护理、配送退货、品牌说明页面；订单查询与邮件订阅显示尚未开放，不收集任何个人信息或显示虚假成功。

## 旧版图片制作记录（已退出当前首页）

内置图像生成工具生成一张横版品牌静物图。最终站点资产：`assets/brand/jewellery-study.webp`，1536×1024。由原始PNG做WebP格式编码，未更改画面内容。原始生成文件保留在本次工作目录，站点仅引用项目内WebP。

最终提示词：

> Original premium editorial still life for a modern stainless-steel jewellery brand. An unbranded polished silver-colour chain draped over pale warm-grey limestone, a sculptural silver-colour cuff and a small brushed gold-colour ring. Fictional concept pieces, not commercial product listings. Soft directional daylight, realistic metal reflections, honed stone texture, warm ivory/stone/silver/champagne palette, central-right composition with breathing room, horizontal 3:2. No text, logos, packaging, people, gemstones, pink/pastels, collage, borders or watermark. Entirely original composition; do not copy an existing brand campaign.

## 本次PDF商品导入

商品名称、材质和钢材牌号、表面工艺／镀层、金银色、戒指尺码、链长、单只／成对、吊坠是否含链、尺寸单位、重量、护理说明、SKU、照片均以PDF及经营者确认资料为准。每个字段需记录文件名／页码；缺失值标待确认，不凭图片猜材质，不生成不存在的选项。

三份目录的703张原始内嵌图片和参数已按型号与目录条目对应；详情保留来源页码，跨页记录未截断。同一型号的多条资料分别展示，不视为已确认库存SKU。分类按型号数字排序，每页24款，支持型号、分类和材质搜索。供应商出厂报价、起订量和联系方式仅留在私有核对数据，不发布为零售售价。详见PDF-IMPORT.md。

100款与Excel批量导入仍在自建后台规划内，本轮不冒充已接通的后台。当前渲染器生成469个真实资料详情页；未启用真实交易。

## 交易准备仍待接通

按已确认范围保留未来游客下单、订单查询和邮件订阅。需补充主体注册地区、支付服务商、正式域名及发信配置、发货地、地区运费时效与退货安排；服务端鉴权、库存、订单、验签回调、退款、邮件确认／退订和后台资源尚未完成。本版本为品牌与商品目录预览，尚不可真实购买。

## 验收

运行README的检查与构建命令。重点检查：469个型号／703条目录记录和图片无遗漏，分类数字排序、分页、型号搜索、条目切换和参数对应正确；项链／吊坠保留空状态；无旧图片或旧商品路由；旧购物袋清理但语言／地区保留；双语与响应式布局正常；源PDF及私有供应商报价不进入dist。

本PR以独立分支预览交付；用户验收后再合并更新正式站。公网检查和浏览器实际结果见PR描述。
