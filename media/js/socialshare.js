/*
Simple Social Share Plugin
*/

function shareToQQ(u, b){
    var e=encodeURIComponent;
    var _t = b;
    var metainfo = document.getElementsByTagName("meta");
    if(_t.length > 120){
        _t= _t.substr(0,117)+'...';
    }
    else{
        _t= _t+'   ';
    }
    var f='http://share.v.t.qq.com/index.php?c=share&a=index&url=';
    var p= ['http://douzhr.com'+e(u)+'&appkey=appkey&pic=&assname=&title='+e(_t)];
    window.open( f+p,'mb', 'width=700, height=680, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, location=yes, resizable=no, status=no' );
}

function shareToSina(u,b)
{
    var s=screen,e=encodeURIComponent;
    var f='http://v.t.sina.com.cn/share/share.php?';
    var p=['url=http://www.douzhr.com'+e(u)+'&title='+e(b)];

    var a=function(){
        if(!window.open(f+p,'mb',['toolbar=0,status=0,resizable=1,width=620,height=450,left=',(s.width-620)/2,',top=',(s.height-450)/2].join('')))u=f+p;
    };

    if(/Firefox/.test(navigator.userAgent))
        {setTimeout(a,0)}
    else
        {a()}
}
    

function shareToRenren(u, t, b)
{
    var e=encodeURIComponent;
    var rrShareParam = {
        resourceUrl : 'http://www.dalei.org'+e(u),   //分享的资源Url
        pic : '',       //分享的主题图片Url
        title : e(t),     //分享的标题
        description : e(b)    //分享的详细描述
    };
    rrShareOnclick(rrShareParam);
}


function shareToDouban(u, t){
    var s=screen,e=encodeURIComponent;
    var f='http://www.douban.com/recommend/?';
    var p=['url=http://www.douzhr.com'+e(u)+'&title='+e(t)];

    var a=function(){
        if(!window.open(f+p,'mb',['toolbar=0,status=0,resizable=1,width=620,height=450,left=',(s.width-620)/2,',top=',(s.height-450)/2].join('')))u=f+p;
    };

    if(/Firefox/.test(navigator.userAgent))
        {setTimeout(a,0)}
    else
        {a()}
}
