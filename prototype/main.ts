let canvas = document.getElementById("screen") as HTMLCanvasElement;
let ctx : CanvasRenderingContext2D = canvas.getContext('2d');

canvas.height = 1000;
canvas.width = 1000;

ctx.fillStyle = 'black';
ctx.fillRect(0, 0, canvas.width, canvas.height);

let rotateXYZ: (x: number, y: number, z: number, theta: number) => number[] = function (
  x: number,
  y: number,	 
  z: number, 
  theta: number
): number[] {
	let sinT:number = Math.sin(theta*Math.PI/180);
	let cosT: number = Math.cos(theta*Math.PI/180);
	let a:number = cosT*(x*cosT - y*sinT) + z*sinT;
	let b:number = cosT*(x*sinT + y*cosT) - sinT*(z*cosT - sinT*(x*cosT - y*sinT));
	let c:number = sinT*( x*sinT + y*cosT ) + cosT*( z*cosT - sinT*( x*cosT - y*sinT ) );
	return [a, b, c];
};


