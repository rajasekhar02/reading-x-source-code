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

// Position of the below line matters check the bottom of the code
const actions = Rx.merge(
  subSelectChange,
  nextButtonClick,
  backButtonClick
).subscribe(() => {
  loading.style.visibility = 'visible';
});

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

function preloadImage(src) {
  return Rx.defer(() => {
    let image = new Image();
    image.src = src;
    let success = Rx.fromEvent(image, 'load').pipe(Rx.map(() => src));
    let failed = Rx.fromEvent(image, 'error').pipe(
      Rx.map(() => LOADING_ERROR_URL)
    );
    return Rx.merge(success, failed);
  });
}
// // ---------------------- INSERT CODE  HERE ---------------------------
// // This "images" Observable is a dummy. Replace it with a stream of each
// // image in the current sub which is navigated by the user.
// loading.style.visibility = 'visible';

const currPosition = Rx.concat(
  Rx.of(0),
  Rx.merge(
    nextButtonClick.pipe(Rx.map(() => 1)),
    backButtonClick.pipe(Rx.map(() => -1))
  ).pipe(Rx.scan((acc, curr) => acc + curr, 0))
);

const images = subSelectChange.pipe(
  Rx.switchMap((sub) =>
    getSubImages(sub).pipe(
      Rx.switchMap((imagesArr) =>
        currPosition.pipe(
          Rx.map((index) => {
            return (index + imagesArr.length) % imagesArr.length;
          }),
          Rx.map((index) => imagesArr[index]),
          Rx.switchMap((imageUrl) => preloadImage(imageUrl))
        )
      )
    )
  )
);

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

// This code make the image viewer to show load even the image is loaded
// const actions = Rx.merge(
//   subSelectChange,
//   nextButtonClick,
//   backButtonClick
// ).subscribe(() => {
//   loading.style.visibility = 'visible';
// });
