const getTestInv = () => {
  let request = new XMLHttpRequest();
  request.open("GET", "product/ajax/dump/", true);
  request.onload = function() {
    if (request.status >= 200 && request.status < 400) {
      let data = JSON.parse(request.responseText);
      data.forEach(function(val, key) {
        paymentOptions_Array.push([
          key,
          val.title,
          // val.imagepath,
          val.price,
          // val.type,
          // val.value,
          // val.alt
        ]);
      });
    }
  };
  request.send();
}
getTestInv();