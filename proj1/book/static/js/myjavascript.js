const TOC_INSERT_SELECTOR = '#toc';              // [セレクター指定] 目次を挿入する要素 querySelector用
const HEADING_SELECTOR    = 'h1,h2,h3,h4,h5,h6'; // [セレクター指定] 収集する見出し要素 querySelectorAll用
const LINK_CLASS_NAME     = 'tocLink link-dark text-decoration-none px-2 fw-bold';           // [クラス名] 目次用aタグに追加するクラス名     .無し
const LINK_CLASS_NAME_LI  = 'link-dark text-decoration-none mt-0 mt-md-2 fs-4_5';  //追加した
const ID_NAME             = 'heading';           // [ID名]    目次に追加するID名のプレフィックス #無し
const tocInsertElement    = document.querySelector(TOC_INSERT_SELECTOR);
const headingElements     = document.querySelectorAll(HEADING_SELECTOR);
const layer = [];
let id = 0;
const uid   = () =>`${ID_NAME}${id++}`;
let oldRank = -1;
try {
    const createLink = (el, rank) => {
        let li = document.createElement('li');
        let a  = document.createElement('a');
        let object  = document.createElement('object');
        el.id  = el.id || uid();
        a.href = `#${el.id}`;
        a.innerText = el.innerText;
        object.id = "mokuji_child"
        object.setAttribute("type","image/svg+xml");
        object.setAttribute("data",SVG_PATH);
        object.setAttribute("width","20");
        object.setAttribute("height","20");

        if (rank == 1) {
          a.className = (LINK_CLASS_NAME + " fs-4_5 lh-xl");
          a.innerHTML = a.innerHTML.substr(2);
          li.className = LINK_CLASS_NAME_LI;
        }else if (rank == 2){
          const LINK_CLASS_NAME     = 'decoration_simple tocLink link-dark text-decoration-none fs-5';
          a.className = LINK_CLASS_NAME;
          li.className = LINK_CLASS_NAME_LI;
        }else{
          const LINK_CLASS_NAME     = 'tocLink link-dark text-decoration-none px-1 fs-5_5';
          a.className = LINK_CLASS_NAME;
          li.appendChild(object);
          li.className = (LINK_CLASS_NAME_LI + " modal-dialog-centered");
        };
        li.appendChild(a);
        return li;
        };
    const findParentElement = (layer, rank, diff) => {
        do {
            rank += diff;
            if (layer[rank]) return layer[rank];
        } while (0 < rank && rank < 7);
        return false;
    };
    const appendToc = (el, toc) => {
        el.appendChild(toc.cloneNode(true));
    };
    const createObject = (el, rank) => {
      if (rank == 3) {
        let object  = document.createElement('object');
        object.id = "object"
        object.setAttribute("type","image/svg+xml");
        object.setAttribute("data",SVG_PATH);
        object.setAttribute("width","34");
        object.setAttribute("height","34");
        // el.insertAdjacentHTML('afterbegin', object);
        // el.insertBefore(object, el.children[0]);
        $(el).wrap('<li class="ps-2 list_center"></li>')
        $(el).before(object);

      }
    };


    headingElements.forEach( (el) => {
        let rank   = Number(el.tagName.substring(1));
        let parent = findParentElement(layer, rank, -1);
        if (oldRank > rank) layer.length = rank + 1;
        if (!layer[rank]) {
            layer[rank] = document.createElement('ol');
            if (parent.lastChild) parent.lastChild.appendChild(layer[rank]);
        }
        layer[rank].appendChild(createLink(el, rank));
        oldRank = rank;
        createObject(el, rank)
    });
    if (layer.length) appendToc(tocInsertElement, findParentElement(layer, 0, 1));





} catch (e) {
    //error
}


// headingElements.forEach( (el) => {
//   if (rank == 2) {
//     a.className = (LINK_CLASS_NAME + " fs-4 lh-xl");
//     a.innerHTML = a.innerHTML.substr(2);
//     li.className = LINK_CLASS_NAME_LI;
//   }

// });// try {
//   const createLink = (el, rank) => {
//     if (rank == 2) {
//       var li = document.createElement('objects');
//     }
//   }
// } catch (e) {
    //error
// }




// var heading_h3 = document.getElementById('heading_h3');

// 追加要素
// var li = document.createElement('a');
// li.innerHTML = 'リスト3';

// 追加  list.children[0]の手前
// heading_h3.insertBefore(li, heading_h3.children[0]);
