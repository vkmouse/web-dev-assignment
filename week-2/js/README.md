### How to run

```node main.js```

### How to install unit test

1. Add jest package

```npm install jest --save-dev```

2. Add following code to package.json

```
  "scripts": {
    "test": "jest"
  }
```

3. Add babel package

```npm install --save-dev @babel/plugin-transform-modules-commonjs```

4. Create ```.babelrc``` and add following code

```
{
  "env": {
    "test": {
      "plugins": ["@babel/plugin-transform-modules-commonjs"]
    }
  }
}
```

### How to run unit test

```npm run test```