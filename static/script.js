document.getElementById("pixelForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const x = document.getElementById("x").value;
    const y = document.getElementById("y").value;
    const color = document.getElementById("color").value;

    fetch("/set_pixel", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ x: x, y: y, color: color })
    })
        .then(res => res.json())
        .then(data => alert("Pixel updated!"))
        .catch(err => alert("Error: " + err));
});