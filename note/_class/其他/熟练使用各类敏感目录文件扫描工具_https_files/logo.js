!function(e,n){"function"==typeof define&&define.amd?define("widget/logo",[],n):e.logo=n()}("undefined"!=typeof self?self:this,function(){function e(){}function n(){var e=null;try{e=window.baidu&&window.baidu.mobads&&window.baidu.mobads.Sdk||window.parent&&parent.baidu&&parent.baidu.mobads&&parent.baidu.mobads.Sdk}catch(n){}return e}function t(e,n){var t=document.createElement("div");t.innerHTML=n;for(var a=document.createDocumentFragment();t.childNodes.length>0;)a.appendChild(t.childNodes[0]);e.appendChild(a)}function a(e,n,t){e.addEventListener?e.addEventListener(n,t,!1):e.attachEvent&&e.attachEvent("on"+n,t)}function o(e){return e.stopPropagation?e.stopPropagation():window.event.cancelBubble=!0,e.preventDefault&&e.preventDefault(),!1}function i(e){var n=null,t=[];for(n in e)e.hasOwnProperty(n)&&t.push(n+"="+encodeURIComponent(e[n]));return t.join("&")}function c(e){e=e||{};var n=e.logoUrl||"http://mssp.baidu.com",a=document.getElementById(e.containerId||"container"),o=document.getElementById(e.feedbackParentId||"container"),i=!e.hideClose&&o,c=e.closeDirect,s=(e.trackingInfo&&e.trackingInfo.dspid,e.deviceType>1?" logo-mobile-container":""),u=['<div class="logo-container'+s+'">','<a href="'+n+'" target="_blank">','<img class="logo-link" src="//cpro.baidustatic.com/cpro/ui/noexpire/ws/images/logo/new-logo@2x_ef70fd1.png" />',"</a>",r(i),"</div>"].join("");if(t(a,u),i){var f=d(o.clientWidth,o.clientHeight);t(o,f),l(e.trackingInfo,c)}}function r(e){return e?['<div class="gap"></div>','<a href="javascript:;" id="logo-close-btn">','<img class="logo-close-img" src="//cpro.baidustatic.com/cpro/ui/noexpire/ws/images/logo/close@2x_86b60c1.png" />',"</a>"].join(""):""}function d(e,n){var t=n-250>0?30:0,a=320;320>e&&e>159?a=160:160>e&&(a=80);var o=160>a?"feedback-container fd-small":"feedback-container",i=s(e,n);return['<div id="feedback-container" class="'+o+'">','<div id="reason-content" class="reason-content" data-reason-num="'+i.length+'" style="width:'+a+"px;padding-top:"+t+'px;">','<div class="intro">反馈意见：</div>',i.join(""),'<a class="fb-btn-cancel" href="javascript:;">返回</a>',"</div>",'<div id="thx-content" class="thx-content">',"<h5>感谢您的反馈！</h5>","<p>您的反馈已记录，我们将努力改善您的浏览体验。</p>","</div>","</div>"].join("")}function s(e,n){function t(){var e=parseInt(3*Math.random(),10);return[a[e],a[3]]}var a=['<a href="javascript:;" data-value="1" class="reason-item">视觉干扰</a>','<a href="javascript:;" data-value="2" class="reason-item">内容不宜</a>','<a href="javascript:;" data-value="3" class="reason-item">不感兴趣</a>','<a href="javascript:;" data-value="0" class="reason-item">其他原因</a>'];return 160>e&&106>n?[]:e>=80&&n>=106&&160>e&&168>n?t():e>=160&&n>=76&&320>e&&106>n?t():a}function l(e,t){var i=document.getElementById("logo-close-btn"),c=document.getElementById("feedback-container"),r=document.getElementById("reason-content"),d=document.getElementById("thx-content");a(i,"click",function(a){var i=n();return i&&t?(i.onAdPlayEnd(),void u(e,0)):(0===+r.getAttribute("data-reason-num")&&(r.style.display="none",u(e,0)),c.style.display="block",o(a))}),a(c,"click",function(t){t=t||window.event;var a=t.target||t.srcElement;if(a&&a.getAttribute)return null!=a.getAttribute("data-value")&&(u(e,a.getAttribute("data-value")),r.style.display="none",d.style.display="block",setTimeout(function(){d.style.display="none"},2e3),setTimeout(function(){var e=n();e&&e.onAdPlayEnd()},4e3)),"fb-btn-cancel"===a.className&&(c.style.display="none"),o(t)})}function u(n,t){var a="https://eclick.baidu.com/close_feedback.jpg?";n=n||{},n.reasonid=t,n._=(new Date).getTime(),a+=i(n);var o=document.createElement("img");o.onerror=e,o.src=a}return{init:c}});
