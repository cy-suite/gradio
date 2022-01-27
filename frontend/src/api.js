function delay(n) {
  return new Promise(function (resolve) {
    setTimeout(resolve, n * 1000);
  });
}

let postData = async (url, body) => {
  const output = await fetch(url, {
    method: "POST",
    body: JSON.stringify(body),
    headers: { "Content-Type": "application/json" }
  });
  return output;
};

export const fn = async (api_endpoint, action, data, queue, queue_callback) => {
  if (queue && ["predict", "interpret"].includes(action)) {
    data["action"] = action;
    const output = await postData(api_endpoint + "queue/push/", data);
    const output_json = await output.json();
    let [hash, queue_position] = [
      output_json["hash"],
      output_json["queue_position"]
    ];
    queue_callback(queue_position, /*is_initial=*/ true);
    let status = "UNKNOWN";
    while (status != "COMPLETE" && status != "FAILED") {
      if (status != "UNKNOWN") {
        await delay(1);
      }
      const status_response = await postData(api_endpoint + "queue/status/", {
        hash: hash
      });
      var status_obj = await status_response.json();
      status = status_obj["status"];
      if (status === "QUEUED") {
        queue_callback(status_obj["data"]);
      } else if (status === "PENDING") {
        queue_callback(null);
      }
    }
    if (status == "FAILED") {
      throw new Error(status);
    } else {
      return status_obj["data"];
    }
  } else {
    const output = await postData(api_endpoint + action + "/", data);
    if (output.status !== 200) {
      throw new Error(output.statusText);
    }
    return await output.json();
  }
};
