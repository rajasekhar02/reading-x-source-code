import * as Rx from 'rxjs';
const nextButton = document.getElementById('next');
const backButton = document.getElementById('back');
const subSelect: HTMLElement = document.getElementById('sub');
const img = document.getElementById('img');
const loading = document.getElementById('loading');

// stackblitz
const LOADING_ERROR_URL =
  'https://jhusain.github.io/reddit-image-viewer/error.png';
const Observable = Rx.Observable;

const subSelectChange = Rx.concat(
  Rx.of(subSelect.value),
  Rx.fromEvent(subSelect, 'change').pipe(
    Rx.map((event: Event) => {
      console.log(event.target.value);
      return event.target.value;
    })
  )
);

const nextButtonClick = Rx.fromEvent(nextButton, 'click');
const backButtonClick = Rx.fromEvent(backButton, 'click');

const actions = new Observable();

// function which returns an array of image URLs for a given reddit sub
// getSubImages("pics") ->
// [
//   "https://upload.wikimedia.org/wikipedia/commons/3/36/Hopetoun_falls.jpg",
//   "https://upload.wikimedia.org/wikipedia/commons/3/38/4-Nature-Wallpapers-2014-1_ukaavUI.jpg",
//   ...
// ]

let fromPromise = (promise) => {
  return new Observable(function (observer) {
    promise
      .then((output) => {
        observer.next(output);
        observer.complete();
      })
      .catch((err) => observer.error(err));
  });
};

function getSubImages(sub) {
  const cachedImages = localStorage.getItem(sub);
  if (cachedImages) {
    return Rx.of(JSON.parse(cachedImages));
  } else {
    const url = `https://www.reddit.com/r/${sub}/.json?limit=200&show=all`;

    // defer ensure new Observable (and therefore) promise gets created
    // for each subscription. This ensures functions like retry will
    // issue additional requests.
    return Rx.defer(() =>
      fromPromise(
        fetch(url)
          .then((res) => res.json())
          .then((data) => {
            const images = data.data.children.map((image) => image.data.url);
            localStorage.setItem(sub, JSON.stringify(images));
            return images;
          })
      )
    );
  }
}

// ---------------------- INSERT CODE  HERE ---------------------------
// This "images" Observable is a dummy. Replace it with a stream of each
// image in the current sub which is navigated by the user.
loading.style.visibility = 'visible';

const currPosition = Rx.merge(
  nextButtonClick.pipe(Rx.map(() => 1)),
  backButtonClick.pipe(Rx.map(() => -1))
).pipe(Rx.scan((acc, curr) => acc + curr, 0));

const images = subSelectChange.pipe(
  Rx.map((sub) =>
    getSubImages(sub).pipe(
      (imagesArr) => currPosition.pipe(Rx.map((index) => imagesArr[index])),
      Rx.switchAll()
    )
  ),
  Rx.switchAll()
);

//  Rx.of(
//   'https://upload.wikimedia.org/wikipedia/commons/3/36/Hopetoun_falls.jpg'
// );

images.subscribe({
  next(url) {
    // hide the loading image
    loading.style.visibility = 'hidden';
    console.log(url);
    // set Image source to URL
    img.src = url;
  },
  error(e) {
    console.error(e);
    alert(
      "I'm having trouble loading the images for that sub. Please wait a while, reload, and then try again later."
    );
  },
});

// This "actions" Observable is a placeholder. Replace it with an
// observable that notfies whenever a user performs an action,
// like changing the sub or navigating the images

actions.subscribe(() => (loading.style.visibility = 'visible'));

// Rx.concat(
//   windowLoad.pipe(Rx.takeUntil(Rx.fromEvent(subSelect, 'change'))),
//   subSelectChange
// ).pipe(
//   Rx.concatMap((selectedValue) => {
//     return getSubImages(selectedValue);
//   })
// );
// Rx.map(() =>
//   subSelectChange.pipe(
//     Rx.concatMap((selectedValue) => {
//       loading.style.visibility = 'visible';
//       // console.log(selectedValue);
//       return getSubImages(selectedValue);
//     }),
//     Rx.mergeMap((imageUrls: string[]) => {
//       currPosition = 0;
//       let newImageUrls = imageUrls;
//       return Rx.merge(
//         Rx.of(newImageUrls[0]),
//         backButtonClick.pipe(
//           Rx.map(() => {
//             if (currPosition == 0) {
//               return newImageUrls[0];
//             }
//             currPosition--;
//             return newImageUrls[currPosition];
//           })
//         ),
//         nextButtonClick.pipe(
//           Rx.map(() => {
//             if (currPosition == newImageUrls.length - 1)
//               return newImageUrls[currPosition];
//             currPosition++;
//             return newImageUrls[currPosition];
//           })
//         )
//       ).pipe(
//         Rx.map((imageUrl) => {
//           if (imageUrl.endsWith('.png') || imageUrl.endsWith('.jpg')) {
//             return imageUrl;
//           }
//           return LOADING_ERROR_URL;
//         })
//       );
//     })
//   )
// );
