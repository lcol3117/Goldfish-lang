
// BEGIN AUTO GOLDFISH
assert = require('assert');
const g_plus = a => b => a + b;
const g_minus = a => b => a - b;
const g_times = a => b => a * b;
const g_div = a => b => a / b;
const g_power = a => b => Math.pow(a, b);
const g_mod = a => b => a % b;
const g_and = a => b => a && b;
const g_or = a => b => a || b;
const g_not = a => !a;
const g_nand = a => b => !(a && b);
const g_nor = a => b => !(a || b);
const g_if = cond => y => n => function(){
  if (cond) {
    return y;
  } else {
    return n;
  }
}();
const g_is = a => b => a === b;
const g_map = l => f => function(){
  return l.map(f);
}();
const g_reduce = l => f => function(){
  return l.reduce((a, x) => f(a)(x));
}();
const g_filter = l => f => function(){
  return l.filter(f);
}();
const g_length = l => l.length
function raw_range(start, end) {
  if(start === end) return [start];
  return [start, ...raw_range(start + 1, end)];
}
const range = start => end => raw_range(start, end - 1);
const g_isnot = a => b => function(){
  return a !== b;
}();
const g_at = l => i => function(){
  return l[i];
}();
// END AUTO GOLDFISH
// This is some example code to see what real code
// looks like written in Goldfish

// The closesttransform function takes
// a list of points
// and returns a list of the distance;
// the respective point to the closest point

const closesttransform = data => function(){
const   g_result = (g_map)(data)((closest)(data));
return g_result;}();
const closest = data => point => function(){
const   dists = (g_map)(data)((dist)(point));
const   distsnotself = (g_filter)(dists)(x => function(){
const     g_result = (g_not)((g_is)(x)(0));
  return g_result;}());
const   g_result = (Math.min)(...distsnotself);
return g_result;}();
const dist = a => b => function(){
const   drange = (range)(0)((g_length)(a));
const   ddists = (g_map)(drange)(x => function(){
const     g_result = (g_power)((g_minus)((g_at)(a)(x))((g_at)(b)(x)))(2);
  return g_result;}());
const   sumd = (g_reduce)(ddists)((g_plus));
const   g_result = (Math.sqrt)(sumd);
return g_result;}();

// test

const dataset = [[1,2],[3,3],[5,17]];

const result = (closesttransform)(dataset);

(console.log)(result);

// The next file (8_closest.gldf) is just the function ;

