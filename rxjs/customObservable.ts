interface Observer {
  next: <T>(value?: T) => void;
  complete: () => void;
  error: (err: Error) => void;
}

interface Subscription {
  unsubscribe: () => void;
}

class Observable {
  private subscribeOnAction: (observer: Observer) => Subscription;
  constructor(subscribeOnAction) {
    this.subscribeOnAction = subscribeOnAction;
  }
  subscribe(observer: Observer): Subscription {
    return this.subscribeOnAction(observer);
  }

  static timeout(time: number): Observable {
    return new Observable(function (observer: Observer): Subscription {
      let handle = setTimeout(() => {
        observer.next();
        observer.complete();
      }, time);
      return {
        unsubscribe: function () {
          clearTimeout(handle);
        },
      };
    });
  }

  retry(num) {
    let self = this;
    return new Observable(function (observer): Subscription {
      let subscriptionHandle:Subscription
      let processRequest = function (value) {
        subscriptionHandle = self.subscribe({
          next(v) {
            observer.next(v);
            observer.complete();
          },
          complete() {
            observer.complete();
          },
          error(err: Error) {
            if (value < num) {
              processRequest(value + 1);
            }
            observer.error(err);
          },
        });
      };
      subscriptionHandle = processRequest(0);
      return subscriptionHandle
    });
  }

  static concat(...observables) {
    return new Observable(function subscribe(observer) {
      let myObservables = observables.slice()
      let currSub = null
      let processObservable = () => {
        if (myObservables.length === 0) {
          observer.complete();
          return;
        }
        let observable = myObservables.shift();
        // observer.next(?) => I can't write this because i don't have the value passed from the observable
        currSub = observable.subscribe({
          next(v) {
            observer.next(v)
          },
          error(err) {
            observer.error(err);
            currSub.unsubscribe()
          },
          complete() {
            processObservable();
          }
        })
      }
      processObservable();
      return {
        unsubscribe() { currSub.unsubscribe()}
      }
    })
  }
}
