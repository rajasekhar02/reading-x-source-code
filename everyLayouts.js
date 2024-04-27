!(function () {
  "use strict";
  class t extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Switcher-${[
              this.threshold,
              this.space,
              this.limit
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${
                this.i
              }"] {\n            gap: ${
                this.space
              };\n          }\n\n          [data-i="${
                this.i
              }"] > * {\n            flex-basis: calc((${
                this.threshold
              } - 100%) * 999);\n          }\n\n          [data-i="${
                this.i
              }"] > :nth-last-child(n+${
                parseInt(this.limit) + 1
              }),\n          [data-i="${this.i}"] > :nth-last-child(n+${
                parseInt(this.limit) + 1
              }) ~ * {\n            flex-basis: 100%;\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get threshold() {
      return this.getAttribute("threshold") || "var(--measure)";
    }
    set threshold(t) {
      return this.setAttribute("threshold", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get limit() {
      return this.getAttribute("limit") || "5";
    }
    set limit(t) {
      return this.setAttribute("limit", t);
    }
    static get observedAttributes() {
      return ["threshold", "space", "limit"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("switcher-l", t);
  class e extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Center-${[
              this.max,
              this.andText,
              this.gutters,
              this.intrinsic
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `
              [data-i="${this.i}"] {
                max-width: ${this.max};
                ${ this.gutters ? `padding-inline-start: ${this.gutters};
                padding-inline-end: ${this.gutters};`
                  : ""
            }
              ${
                this.andText ? "text-align: center;" : ""
              }\n            ${
                this.intrinsic
                  ? "\n            display: flex;\n            flex-direction: column;\n            align-items: center;"
                  : ""
              }\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get max() {
      return this.getAttribute("max") || "var(--measure)";
    }
    set max(t) {
      return this.setAttribute("max", t);
    }
    get andText() {
      return this.hasAttribute("andText");
    }
    set andText(t) {
      return t
        ? this.setAttribute("andText", "")
        : this.removeAttribute("andText");
    }
    get gutters() {
      return this.getAttribute("gutters") || null;
    }
    set gutters(t) {
      return this.setAttribute("gutters", t);
    }
    get intrinsic() {
      return this.hasAttribute("intrinsic");
    }
    set intrinsic(t) {
      return t
        ? this.setAttribute("intrinsic", "")
        : this.removeAttribute("intrinsic");
    }
    static get observedAttributes() {
      return ["max", "andText", "gutters", "intrinsic"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("center-l", e);
  class i extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Cover-${[
              this.centered,
              this.space,
              this.minHeight,
              this.noPad
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${
                this.i
              }"] {\n            min-height: ${
                this.minHeight
              };\n            padding: ${
                this.noPad ? "0" : this.space
              };\n          }\n      \n          [data-i="${
                this.i
              }"] > * {\n            margin-block: ${
                this.space
              };\n          }\n      \n          [data-i="${
                this.i
              }"] > :first-child:not(${
                this.centered
              }) {\n            margin-block-start: 0;\n          }\n      \n          [data-i="${
                this.i
              }"] > :last-child:not(${
                this.centered
              }) {\n            margin-block-end: 0;\n          }\n      \n          [data-i="${
                this.i
              }"] > ${
                this.centered
              } {\n            margin-block: auto;\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get centered() {
      return this.getAttribute("centered") || "h1";
    }
    set centered(t) {
      return this.setAttribute("centered", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get minHeight() {
      return this.getAttribute("minHeight") || "100vh";
    }
    set minHeight(t) {
      return this.setAttribute("minHeight", t);
    }
    get noPad() {
      return this.hasAttribute("noPad");
    }
    set noPad(t) {
      return t ? this.setAttribute("noPad", "") : this.removeAttribute("noPad");
    }
    static get observedAttributes() {
      return ["centered", "space", "minHeight", "noPad"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("cover-l", i);
  class s extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Stack-${[
              this.space,
              this.recursive,
              this.splitAfter
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${this.i}"]${
                this.recursive ? "" : " >"
              } * + * {\n            margin-block-start: ${
                this.space
              };\n          }\n      \n          ${
                this.splitAfter
                  ? `\n            [data-i="${this.i}"]:only-child {\n              block-size: 100%;\n            }\n      \n            [data-i="${this.i}"] > :nth-child(${this.splitAfter}) {\n              margin-block-end: auto;\n            }`
                  : ""
              }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get recursive() {
      return this.hasAttribute("recursive");
    }
    set recursive(t) {
      return this.setAttribute(t ? "recursive" : "");
    }
    get splitAfter() {
      return this.getAttribute("splitAfter") || null;
    }
    set splitAfter(t) {
      return this.setAttribute("splitAfter", t);
    }
    static get observedAttributes() {
      return ["space", "recursive", "splitAfter"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("stack-l", s);
  class n extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Box-${[
              this.padding,
              this.borderWidth,
              this.invert
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${
                this.i
              }"] {\n            padding: ${
                this.padding
              };\n            border: ${this.borderWidth} solid;\n            ${
                this.invert
                  ? "background-color: var(--color-light);\n              filter: invert(100%);"
                  : ""
              }\n          }\n      \n          [data-i="${
                this.i
              }"] {\n            background-color: inherit;\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get padding() {
      return this.getAttribute("padding") || "var(--s1)";
    }
    set padding(t) {
      return this.setAttribute("padding", t);
    }
    get borderWidth() {
      return this.getAttribute("borderWidth") || "var(--border-thin)";
    }
    set borderWidth(t) {
      return this.setAttribute("borderWidth", t);
    }
    static get observedAttributes() {
      return ["borderWidth", "padding", "invert"];
    }
    get invert() {
      return this.hasAttribute("invert");
    }
    set invert(t) {
      return t
        ? this.setAttribute("invert", "")
        : this.removeAttribute("invert");
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("box-l", n);
  class r extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Cluster-${[this.justify, this.align, this.space].join(
              ""
            )}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML =
                `\n          [data-i="${this.i}"] {\n            justify-content: ${this.justify};\n            align-items: ${this.align};\n            gap: ${this.space};\n          }\n        `
                  .replace(/\s\s+/g, " ")
                  .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get justify() {
      return this.getAttribute("justify") || "flex-start";
    }
    set justify(t) {
      return this.setAttribute("justify", t);
    }
    get align() {
      return this.getAttribute("align") || "flex-start";
    }
    set align(t) {
      return this.setAttribute("align", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    static get observedAttributes() {
      return ["justify", "align", "space"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("cluster-l", r);
  class a extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Grid-${[this.min, this.space].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML =
                `\n          [data-i="${this.i}"] {\n            grid-gap: ${this.space};\n          }\n\n          @supports (width: min(${this.min}, 100%)) {\n            [data-i="${this.i}"] {\n              grid-template-columns: repeat(auto-fill, minmax(min(${this.min}, 100%), 1fr));\n            }\n          }\n        `
                  .replace(/\s\s+/g, " ")
                  .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get min() {
      return this.getAttribute("min") || "250px";
    }
    set min(t) {
      return this.setAttribute("min", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    static get observedAttributes() {
      return ["min", "space"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("grid-l", a);
  class u extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            (this.contentMin.includes("%") ||
              console.warn(
                "The value for each <sidebar-l> `contentMin` property should be a percentage. Otherwise overflow is likely to occur"
              ),
            (this.i = `Sidebar-${[
              this.side,
              this.sideWidth,
              this.contentMin,
              this.space
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${
                this.i
              }"] {\n            gap: ${this.space};\n            ${
                this.noStretch ? "align-items: flex-start;" : ""
              }\n          }\n      \n          [data-i="${
                this.i
              }"] > * {\n            ${
                this.sideWidth ? `flex-basis: ${this.sideWidth};` : ""
              }\n          }\n      \n          [data-i="${this.i}"] > ${
                "left" !== this.side ? ":first-child" : ":last-child"
              } {\n            flex-basis: 0;\n            flex-grow: 999;\n            min-inline-size: ${
                this.contentMin
              };\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get side() {
      return this.getAttribute("side") || "left";
    }
    set side(t) {
      return this.setAttribute("side", t);
    }
    get sideWidth() {
      return this.getAttribute("sideWidth") || null;
    }
    set sideWidth(t) {
      return this.setAttribute("sideWidth", t);
    }
    get contentMin() {
      return this.getAttribute("contentMin") || "50%";
    }
    set contentMin(t) {
      return this.setAttribute("contentMin", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s1)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get noStretch() {
      return this.hasAttribute("noStretch");
    }
    set noStretch(t) {
      t
        ? this.setAttribute("noStretch", "")
        : this.removeAttribute("noStretch");
    }
    static get observedAttributes() {
      return ["side", "sideWidth", "contentMin", "space", "noStretch"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback(t) {
      this.render();
    }
  }
  "customElements" in window && customElements.define("sidebar-l", u);
  class h extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            (1 !== this.children.length &&
              console.warn(
                "<frame-l> elements should have just one child element"
              ),
            (this.i = `Frame-${[this.ratio].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = this.ratio.split(":"),
              e = document.createElement("style");
            (e.id = this.i),
              (e.innerHTML =
                `\n          [data-i="${this.i}"] {\n            aspect-ratio: ${t[0]} / ${t[1]};\n          }\n        `
                  .replace(/\s\s+/g, " ")
                  .trim()),
              document.head.appendChild(e);
          }
        });
    }
    get ratio() {
      return this.getAttribute("ratio") || "16:9";
    }
    set ratio(t) {
      return this.setAttribute("ratio", t);
    }
    static get observedAttributes() {
      return ["ratio"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("frame-l", h);
  class d extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            ((this.i = `Reel-${[
              this.itemWidth,
              this.height,
              this.space,
              this.noBar
            ].join("")}`),
            (this.dataset.i = this.i),
            !document.getElementById(this.i))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML = `\n          [data-i="${
                this.i
              }"] {\n            height: ${
                this.height
              };\n          }\n      \n          [data-i="${
                this.i
              }"] > * {\n            flex: 0 0 ${
                this.itemWidth
              };\n          }\n      \n          [data-i="${
                this.i
              }"] > img {\n            height: 100%;\n            flex-basis: auto;\n            width: auto;\n          }\n      \n          [data-i="${
                this.i
              }"] > * + * {\n            margin-inline-start: ${
                this.space
              };\n          }\n      \n          [data-i="${
                this.i
              }"].overflowing {\n            ${
                this.noBar ? "" : `padding-bottom: ${this.space}`
              }\n          }\n      \n          ${
                this.noBar
                  ? `\n          [data-i="${this.i}"] {\n            scrollbar-width: none;\n          }\n          \n          [data-i="${this.i}"]::-webkit-scrollbar {\n            display: none;\n          }\n          `
                  : ""
              }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(t);
          }
        });
    }
    toggleOverflowClass(t) {
      t.classList.toggle("overflowing", this.scrollWidth > this.clientWidth);
    }
    get itemWidth() {
      return this.getAttribute("itemWidth") || "auto";
    }
    set itemWidth(t) {
      return this.setAttribute("itemWidth", t);
    }
    get height() {
      return this.getAttribute("height") || "auto";
    }
    set height(t) {
      return this.setAttribute("height", t);
    }
    get space() {
      return this.getAttribute("space") || "var(--s0)";
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get noBar() {
      return this.hasAttribute("noBar");
    }
    set noBar(t) {
      t ? this.setAttribute("noBar", "") : this.removeAttribute("noBar");
    }
    static get observedAttributes() {
      return ["itemWidth", "height", "space", "noBar"];
    }
    connectedCallback() {
      this.render(),
        "ResizeObserver" in window &&
          new ResizeObserver(t => {
            this.toggleOverflowClass(t[0].target);
          }).observe(this),
        "MutationObserver" in window &&
          new MutationObserver(t => {
            this.toggleOverflowClass(t[0].target);
          }).observe(this, { childList: !0 });
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("reel-l", d);
  class c extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          (this.i = `Imposter-${[this.breakout, this.fixed, this.margin].join(
            ""
          )}`),
            (this.dataset.i = this.i);
          let t = "0" === this.margin ? "0px" : this.margin;
          if (
            !document.getElementById(this.i) &&
            (!this.breakout || this.fixed)
          ) {
            let e = document.createElement("style");
            (e.id = this.i),
              (e.innerHTML = `\n          [data-i="${this.i}"] {\n            ${
                this.breakout
                  ? ""
                  : `\n              max-inline-size: calc(100% - (${t} * 2));\n              max-block-size: calc(100% - (${t} * 2));\n              overflow: auto;`
              }\n            ${
                this.fixed ? "\n              position: fixed;" : ""
              }\n          }\n        `
                .replace(/\s\s+/g, " ")
                .trim()),
              document.head.appendChild(e);
          }
        });
    }
    get breakout() {
      return this.hasAttribute("breakout");
    }
    set breakout(t) {
      return t
        ? this.setAttribute("breakout", "")
        : this.removeAttribute("breakout");
    }
    get fixed() {
      return this.hasAttribute("fixed");
    }
    set fixed(t) {
      return t ? this.setAttribute("fixed", "") : this.removeAttribute("fixed");
    }
    get margin() {
      return this.getAttribute("margin") || "0px";
    }
    set margin(t) {
      return this.setAttribute("margin", t);
    }
    static get observedAttributes() {
      return ["breakout", "margin", "fixed"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  "customElements" in window && customElements.define("imposter-l", c);
  class l extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          if (
            (this.label &&
              (this.setAttribute("role", "img"),
              this.setAttribute("aria-label", this.label)),
            this.space &&
              ((this.i = `Icon-${this.space}`),
              (this.dataset.i = this.i),
              !document.getElementById(this.i)))
          ) {
            let t = document.createElement("style");
            (t.id = this.i),
              (t.innerHTML =
                `\n            [data-i="${this.i}"] {\n              display: inline-flex;\n              align-items: baseline;\n            }\n\n            [data-i="${this.i}"] > svg {\n              margin-inline-end: ${this.space};\n            }\n          `
                  .replace(/\s\s+/g, " ")
                  .trim()),
              document.head.appendChild(t);
          }
        });
    }
    get space() {
      return this.getAttribute("space") || null;
    }
    set space(t) {
      return this.setAttribute("space", t);
    }
    get label() {
      return this.getAttribute("label") || null;
    }
    set label(t) {
      return this.setAttribute("label", t);
    }
    static get observedAttributes() {
      return ["space", "label"];
    }
    connectedCallback() {
      this.render();
    }
    attributeChangedCallback() {
      this.render();
    }
  }
  function o(t) {
    if (!t.includes(",")) return parseInt(t);
    const e = t.split(",").map(t => parseInt(t));
    return Math.floor(Math.random() * (e[1] - e[0] + 1)) + e[0];
  }
  "customElements" in window && customElements.define("icon-l", l);
  class m extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          const t = (function (t) {
            const e = [
                "morbi",
                "in",
                "ex",
                "sit",
                "amet",
                "quam",
                "bibendum",
                "semper",
                "donec",
                "accumsan",
                "enim",
                "nibh",
                "vel",
                "laoreet",
                "eros",
                "feugiat",
                "sodales",
                "nullam",
                "feugiat",
                "mi",
                "vitae",
                "tincidunt",
                "iaculis",
                "vestibulum",
                "ante",
                "ipsum",
                "primis",
                "in",
                "faucibus",
                "orci",
                "luctus",
                "et",
                "ultrices",
                "posuere",
                "cubilia",
                "curae",
                "quisque",
                "vulputate",
                "nisi",
                "eu",
                "imperdiet",
                "venenatis",
                "lacus",
                "sapien",
                "tempus",
                "nibh",
                "ac",
                "pretium",
                "quam",
                "dolor",
                "nec",
                "tellus",
                "sed",
                "a",
                "mauris",
                "efficitur",
                "vehicula",
                "lacus",
                "non",
                "varius",
                "arcu",
                "proin",
                "consequat",
                "quam",
                "eu",
                "vulputate",
                "tincidunt",
                "dolor",
                "leo",
                "pretium",
                "arcu",
                "ut",
                "euismod",
                "nisl",
                "sapien",
                "nec",
                "lorem",
                "fusce",
                "nec",
                "orci",
                "in",
                "enim",
                "commodo",
                "tristique",
                "mauris",
                "ornare",
                "ante",
                "vitae",
                "sapien",
                "tempus",
                "sit",
                "amet",
                "porttitor",
                "ante",
                "egestas",
                "in",
                "malesuada",
                "tellus",
                "orci",
                "eget",
                "ultricies",
                "ipsum",
                "ultrices",
                "ac",
                "phasellus",
                "nec",
                "felis",
                "nibh",
                "morbi",
                "convallis",
                "luctus",
                "ipsum",
                "nec",
                "interdum",
                "pellentesque",
                "ultrices",
                "ligula",
                "erat",
                "non",
                "sollicitudin",
                "odio",
                "auctor",
                "at",
                "duis",
                "ac",
                "diam",
                "id",
                "dui",
                "blandit",
                "tempus",
                "eget",
                "sed",
                "erat",
                "curabitur",
                "euismod",
                "varius",
                "neque",
                "cras",
                "ac",
                "justo",
                "congue",
                "mattis",
                "urna",
                "ornare",
                "semper",
                "mi"
              ],
              i = o(t),
              s = [];
            for (let t = 1; t <= i; t++)
              s.push(`<span>${e[Math.floor(Math.random() * e.length)]}</span>`);
            return s.join(" ");
          })(this.words);
          this.innerHTML = `<p>${t}</p>`;
        });
    }
    static get observedAttributes() {
      return ["words"];
    }
    attributeChangedCallback() {
      this.render();
    }
    connectedCallback() {
      this.render();
    }
    get words() {
      return this.getAttribute("words") || "15,20";
    }
    set words(t) {
      return this.setAttribute("words", t);
    }
  }
  "customElements" in window && customElements.define("text-l", m);
  class b extends HTMLElement {
    constructor() {
      super(),
        (this.render = () => {
          (this.i = `Image-${[this.ratio, this.minWidth, this.maxWidth].join(
            ""
          )}`),
            (this.dataset.i = this.i),
            document.getElementById(this.i) ||
              (document.head.innerHTML += `\n        <style id="${
                this.i
              }">\n          [data-i="${this.i}"] {\n            max-width: ${
                this.maxWidth
              };\n            min-width: ${
                this.minWidth
              };            \n          }\n\n          [data-i="${
                this.i
              }"]::after {\n            padding-top: ${
                (function (t) {
                  const e = t.split(":").map(t => parseInt(t));
                  return (e[0] / e[1]) * 100;
                })(this.ratio) + "%"
              };\n          }\n        </style>\n        `);
        });
    }
    static get observedAttributes() {
      return ["ratio", "minWidth", "maxWidth"];
    }
    get ratio() {
      return this.getAttribute("ratio") || "6:9";
    }
    set ratio(t) {
      return this.setAttribute("ratio", t);
    }
    get minWidth() {
      return this.getAttribute("minWidth") || "0";
    }
    set minWidth(t) {
      return this.setAttribute("minWidth", t);
    }
    get maxWidth() {
      return this.getAttribute("maxWidth") || "none";
    }
    set maxWidth(t) {
      return this.setAttribute("maxWidth", t);
    }
    attributeChangedCallback() {
      this.setAttribute("aria-label", `Image with ${this.ratio} ratio`),
        this.render();
    }
    connectedCallback() {
      this.setAttribute("role", "img"), this.render();
    }
  }
  "customElements" in window && customElements.define("image-l", b);
  class g extends HTMLElement {
    constructor() {
      super(),
        (this.generate = () => {
          let t = (function (t) {
            const e = [
                "morbi",
                "in",
                "ex",
                "sit",
                "amet",
                "quam",
                "bibendum",
                "semper",
                "donec",
                "accumsan",
                "enim",
                "nibh",
                "vel",
                "laoreet",
                "eros",
                "feugiat",
                "sodales",
                "nullam",
                "feugiat",
                "mi",
                "vitae",
                "tincidunt",
                "iaculis",
                "vestibulum",
                "ante",
                "ipsum",
                "primis",
                "in",
                "faucibus",
                "orci",
                "luctus",
                "et",
                "ultrices",
                "posuere",
                "cubilia",
                "curae",
                "quisque",
                "vulputate",
                "nisi",
                "eu",
                "imperdiet",
                "venenatis",
                "lacus",
                "sapien",
                "tempus",
                "nibh",
                "ac",
                "pretium",
                "quam",
                "dolor",
                "nec",
                "tellus",
                "sed",
                "a",
                "mauris",
                "efficitur",
                "vehicula",
                "lacus",
                "non",
                "varius",
                "arcu",
                "proin",
                "consequat",
                "quam",
                "eu",
                "vulputate",
                "tincidunt",
                "dolor",
                "leo",
                "pretium",
                "arcu",
                "ut",
                "euismod",
                "nisl",
                "sapien",
                "nec",
                "lorem",
                "fusce",
                "nec",
                "orci",
                "in",
                "enim",
                "commodo",
                "tristique",
                "mauris",
                "ornare",
                "ante",
                "vitae",
                "sapien",
                "tempus",
                "sit",
                "amet",
                "porttitor",
                "ante",
                "egestas",
                "in",
                "malesuada",
                "tellus",
                "orci",
                "eget",
                "ultricies",
                "ipsum",
                "ultrices",
                "ac",
                "phasellus",
                "nec",
                "felis",
                "nibh",
                "morbi",
                "convallis",
                "luctus",
                "ipsum",
                "nec",
                "interdum",
                "pellentesque",
                "ultrices",
                "ligula",
                "erat",
                "non",
                "sollicitudin",
                "odio",
                "auctor",
                "at",
                "duis",
                "ac",
                "diam",
                "id",
                "dui",
                "blandit",
                "tempus",
                "eget",
                "sed",
                "erat",
                "curabitur",
                "euismod",
                "varius",
                "neque",
                "cras",
                "ac",
                "justo",
                "congue",
                "mattis",
                "urna",
                "ornare",
                "semper",
                "mi"
              ],
              i = o(t),
              s = [];
            for (let t = 0; t < i; t++)
              s.push(e[Math.floor(Math.random() * e.length)]);
            return s;
          })(this.count);
          return (
            this.capitalize &&
              (t = t.map(t => t.charAt(0).toUpperCase() + t.slice(1))),
            this.sentence &&
              ((t[0] = t[0].charAt(0).toUpperCase() + t[0].slice(1)),
              t[0].toUpperCase(),
              (t[t.length - 1] += ". ")),
            t.join(" ")
          );
        }),
        (this.render = () => {
          this.innerHTML = "";
          const t = this.repeat ? o(this.repeat) : 1;
          for (let e = 0; e < t; e++) this.innerHTML += this.generate();
        });
    }
    static get observedAttributes() {
      return ["count", "sentence", "capitalize", "repeat"];
    }
    attributeChangedCallback() {
      this.render();
    }
    connectedCallback() {
      this.render();
    }
    get count() {
      return this.getAttribute("count") || "2,3";
    }
    set count(t) {
      return this.setAttribute("count", t);
    }
    get sentence() {
      return this.hasAttribute("sentence");
    }
    set sentence(t) {
      t ? this.setAttribute("sentence", "") : this.removeAttribute("sentence");
    }
    get capitalize() {
      return this.hasAttribute("capitalize");
    }
    set capitalize(t) {
      t
        ? this.setAttribute("capitalize", "")
        : this.removeAttribute("capitalize");
    }
    get repeat() {
      this.getAttribute("repeat");
    }
    set repeat(t) {
      this.setAttribute("repeat", t);
    }
  }
  "customElements" in window && customElements.define("words-l", g);
})();
