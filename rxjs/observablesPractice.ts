import './style.css';

import {
  of,
  map,
  timer,
  takeUntil,
  fromEvent,
  Observable,
  concatMap,
  interval,
  debounce,
  takeLast,
  from,
  concatAll,
  distinctUntilChanged,
  switchMap,
} from 'rxjs';
import { switchAll, switchScan, throttle } from 'rxjs/operators';
import * as Rx from 'rxjs';

of('World')
  .pipe(map((name) => `Hello, ${name}!`))
  .subscribe(console.log);
let outputElement = document.createElement('span');
let buttonElement = document.createElement('button');
let inputElement = document.createElement('input');
buttonElement.innerText = 'Stop Timer';
document.body.prepend(outputElement);
document.body.prepend(buttonElement);
document.body.prepend(inputElement);

// let mouseDown = fromEvent(document.body, 'mousedown');
// let mouseMove = fromEvent(document.body, 'mousemove');
// let mouseUp = fromEvent(document.body, 'mouseup');
let mouseClick = fromEvent(buttonElement, 'click');
// mouseDown
//   .pipe(
//     concatMap((downEvent: MouseEvent) => {
//       // clickedPoint = downEvent;
//       return mouseMove.pipe(
//         takeUntil(mouseUp),
//         map((moveEvent: MouseEvent) => {
//           return {
//             customX: moveEvent.clientX - downEvent.offsetX,
//             customY: moveEvent.clientY - downEvent.offsetY,
//           };
//         })
//       );
//     })
//     // concatAll()
//   )
//   .subscribe((moveEvent) => {
//     // console.log(moveEvent.clientY);
//     buttonElement.style.position = 'absolute';
//     buttonElement.style.left = moveEvent.customX + 'px';
//     buttonElement.style.top = moveEvent.customY + 'px';
//   });

function searchWikipedia(term) {
  let url = `https://en.wikipedia.org/api/rest_v1/page/title/${term}`;
  return new Observable(function (observer) {
    const controller = new AbortController();
    const { signal } = controller;
    fetch(url, { signal })
      .then((result) => {
        observer.next(result);
        observer.complete();
      })
      .catch((err) => {
        observer.error(new Error('error occured'));
      });
    return {
      unsubscribe: function () {
        controller.abort();
      },
    };
  });
}

let keyPressEvent = fromEvent(inputElement, 'keypress');
keyPressEvent
  .pipe(
    debounce(() => interval(500)),
    map((event: KeyboardEvent) => {
      console.log(inputElement.value);
      return inputElement.value;
    }),
    distinctUntilChanged(),
    map(() =>
      searchWikipedia(inputElement.value).pipe(
        switchMap((response: Response) => {
          return new Observable(function (observer) {
            response
              .json()
              .then((jsonObj) => {
                observer.next(jsonObj);
                observer.complete();
              })
              .catch((err) => observer.error(err));
          });
        })
      )
    ),
    switchAll()
  )
  .subscribe((outputJSON) => {
    console.log(outputJSON);
  });

let setIntervalObservable = function (interval, stopAfterTime, caller) {
  return new Observable(function (observer) {
    let handle = setInterval(
      function (caller) {
        observer.next(caller);
      },
      interval,
      caller
    );
    setTimeout(function () {
      clearInterval(handle);
      observer.complete();
    }, stopAfterTime);
    return {
      unsubscribe: function () {
        clearInterval(handle);
      },
    };
  });
};

let getRandomInt = function (min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); // The maximum is exclusive and the minimum is inclusive
};

setIntervalObservable(1000, 5000, 'caller')
  .pipe(
    Rx.map((value) => {
      let start = getRandomInt(1000, 12000);
      let end = getRandomInt(start + 1, 15000);
      console.log(start, end);
      return setIntervalObservable(start, end, `sub-caller ${start}-${end}`);
    })
  )
  .pipe(
    Rx.map((task) => {
      return Rx.concat(
        Rx.of(1),
        task.pipe(
          Rx.filter(() => false),
          Rx.catchError(() => new Observable())
        ),
        Rx.of(-1)
      );
    }),
    Rx.mergeAll(),
    Rx.scan((acc: number, curr: number) => acc + curr),
    Rx.map((x) => x == 0),
    Rx.distinctUntilChanged()
  )
  .subscribe((x) => console.log(x));
