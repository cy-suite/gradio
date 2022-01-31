export function get_domains(values) {
  let _vs;
  if (Array.isArray(values)) {
    _vs = values.reduce((acc, { values }) => {
      return [...acc, ...values.map(({ x, y }) => y)];
    }, []);
  } else {
    _vs = values.values;
  }
  return [Math.min(..._vs), Math.max(..._vs)];
}

export function transform_values(values, x, y) {
  const transformed_values = Object.entries(values[0]).reduce((acc, next, i) => {
    if ((!x && i === 0) || (x && next[0] === x)) {
      acc.x.name = next[0];
    } else if (!y || y && y.includes(next[0]) ) {
      acc.y.push({name: next[0], values: []});
    }
    return acc;
  }, {x: {name: '', values: []}, y: []});

  for (let i = 0; i < values.length; i++) {
    const _a = Object.entries(values[i]);
    for (let j = 0; j < _a.length; j++) {
      let [name, x] = _a[j];
      if (name === transformed_values.x.name) {
        transformed_values.x.values.push(x);
      } else {
        transformed_values.y[j - 1].values.push({ y: _a[j][1], x: _a[0][1] });
      }
    }
  }

  return transformed_values;
}

let c = 0;
export function get_color() {
  let default_colors = [
    [255, 99, 132],
    [54, 162, 235],
    [240, 176, 26],
    [153, 102, 255],
    [75, 192, 192],
    [255, 159, 64],
  ];

  if (c >= default_colors.length) c = 0;

  const [r, g, b] = default_colors[c++];

  return `rgb(${r},${g},${b})`;
}
