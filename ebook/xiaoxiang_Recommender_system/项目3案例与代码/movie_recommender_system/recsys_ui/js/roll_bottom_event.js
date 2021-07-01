
/**
 * @author Dong Changqing
 * 自定义事件回调函数
 */
function roll_bottom_event() {
   /* alert("roll_bottom_event");*/
}
/**
 * @author Dong Changqing
 * 自定义事件绑定
 */
var timeoutInt;
window.onscroll = function () {
    setTimeout(function () {
        if (timeoutInt != undefined) {
            window.clearTimeout(timeoutInt);
        }
        timeoutInt = window.setTimeout(function () {
        	
            //监听事件内容
            if(getScrollHeight() < getDocumentTop() + getWindowHeight() + 1000){
                //当滚动条到底时,这里是触发内容
                //异步请求数据,局部刷新dom
            	roll_bottom_event();
            }
        }, 105);
    }, 100);
}

/**
 * @author Dong Changqing
 * 文档高度
 */
function getDocumentTop() {
    var scrollTop =  0, bodyScrollTop = 0, documentScrollTop = 0;
    if (document.body) {
        bodyScrollTop = document.body.scrollTop;
    }
    if (document.documentElement) {
        documentScrollTop = document.documentElement.scrollTop;
    }
    scrollTop = (bodyScrollTop - documentScrollTop > 0) ? bodyScrollTop : documentScrollTop;
   /* console.log("scrollTop:"+scrollTop);*/
    return scrollTop;
}

/**
 * @author Dong Changqing
 * 可视窗口高度
 */
function getWindowHeight() {
    var windowHeight = 0;
    if (document.compatMode == "CSS1Compat") {
        windowHeight = document.documentElement.clientHeight;
    } else {
        windowHeight = document.body.clientHeight;
    }
   /* console.log("windowHeight:"+windowHeight);*/
    return windowHeight;
}

/**
 * @author Dong Changqing
 * 滚动条滚动高度
 */
function getScrollHeight() {
    var scrollHeight = 0, bodyScrollHeight = 0, documentScrollHeight = 0;
    if (document.body) {
        bodyScrollHeight = document.body.scrollHeight;
    }
    if (document.documentElement) {
        documentScrollHeight = document.documentElement.scrollHeight;
    }
    scrollHeight = (bodyScrollHeight - documentScrollHeight > 0) ? bodyScrollHeight : documentScrollHeight;
    /*console.log("scrollHeight:"+scrollHeight);*/
    return scrollHeight;
}