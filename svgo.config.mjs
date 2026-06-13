// SVG optimisation for the distributed logo.
// preset-default already keeps the viewBox and <title> in svgo v4; here we only
// trim coordinate precision and re-assert role="img" for accessibility.
export default {
  multipass: true,
  js2svg: { indent: 2, pretty: true },
  plugins: [
    {
      name: 'preset-default',
      params: {
        overrides: {
          cleanupNumericValues: { floatPrecision: 2 },
          convertPathData: { floatPrecision: 2 },
        },
      },
    },
    { name: 'addAttributesToSVGElement', params: { attributes: [{ role: 'img' }] } },
  ],
};
