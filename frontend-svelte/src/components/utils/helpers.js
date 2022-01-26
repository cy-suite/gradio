// import mime from "mime-types";

export const playable = (filename) => {
  // let video_element = document.createElement("video");
  // let mime_type = mime.lookup(filename);
  // return video_element.canPlayType(mime_type) != "";
  return true; // FIX BEFORE COMMIT - mime import causing issues
};

export const deepCopy = (obj) => {
  return JSON.parse(JSON.stringify(obj));
}

export function randInt(min, max) {
  return Math.floor(Math.random() * (max - min) + min);
}

export const getNextColor = (index, alpha) => {
  alpha = alpha || 1;
  let default_colors = [
    [255, 99, 132],
    [54, 162, 235],
    [240, 176, 26],
    [153, 102, 255],
    [75, 192, 192],
    [255, 159, 64],
    [194, 88, 74],
    [44, 102, 219],
    [44, 163, 23],
    [191, 46, 217],
    [160, 162, 162],
    [163, 151, 27],
  ];
  if (index < default_colors.length) {
    var color_set = default_colors[index];
  } else {
    var color_set = [randInt(64, 196), randInt(64, 196), randInt(64, 196)];
  }
  return (
    "rgba(" +
    color_set[0] +
    ", " +
    color_set[1] +
    ", " +
    color_set[2] +
    ", " +
    alpha +
    ")"
  );
}

export const prettyBytes = (bytes) => {
  let units = ["B", "KB", "MB", "GB", "PB"];
  let i = 0;
  while (bytes > 1024) {
    bytes /= 1024;
    i++;
  }
  let unit = units[i];
  return bytes.toFixed(1) + " " + unit;
}

