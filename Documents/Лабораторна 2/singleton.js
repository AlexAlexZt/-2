class Singleton {
  constructor() {
    if (!Singleton.instance) {
      Singleton.instance = this;
    }

    return Singleton.instance;
  }

  someMethod() {
    console.log("Виконується метод в класі Singleton");
  }
}

const instance = new Singleton();
Object.freeze(instance);

module.exports = instance;

