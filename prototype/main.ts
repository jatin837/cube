let canvas = document.getElementById("screen") as HTMLCanvasElement;
let ctx : CanvasRenderingContext2D = canvas.getContext('2d');

canvas.height = 1000;
canvas.width = 1000;

ctx.fillStyle = 'black';
ctx.fillRect(0, 0, canvas.width, canvas.height);





