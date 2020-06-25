print("Welcome to the Goldfish -> JavaScript compiler!")
filename = input("Enter the file to compile (_.gldf):")
print("Compiling `"+filename+"`...")
goldfish_file = open(filename, "r")
new = goldfish_file.read()
goldfish_file.close()
cn_d = "assert(g_null === null, \"Null Check Failed!\")"
new = new.replace("~>>", "~ >>")
new = new.replace("~ >>", "g_null >>")
new = new.replace("~", "null")
new = new.replace("+", "g_plus")
new = new.replace("-", "g_minus")
new = new.replace("*", "g_times")
new = new.replace("/", "g_div")
new = new.replace("^", "g_power")
new = new.replace("%", "g_mod")
new = new.replace("(and", "(g_and")
new = new.replace("(or", "(g_or")
new = new.replace("(not", "(g_not")
new = new.replace("(nand", "(g_nand")
new = new.replace("(nor", "(g_nor")
new = new.replace("(if", "(g_if")
new = new.replace("(is", "(g_is")
new = new.replace("(isnot", "(g_isnot")
new = new.replace("(map", "(g_map")
new = new.replace("(reduce", "(g_reduce")
new = new.replace("(filter", "(g_filter")
new = new.replace("(length", "(g_length")
new = new.replace("(at", "(g_at")
new = new.replace(" | ", "|")
new = new.replace(">>", "=>")
new = new.replace("@", "g_result")
new = new.replace("{", "function(){")
new = new.replace("}", "return g_result;}()")
new = new.replace("|", ")(")
new = new.replace(":", "\"")
new = new.replace(";;", "//")
new = new.replace("&checknull", cn_d)
final = ""
for i in new.split("\n"):
  if "<<" in i:
    final += "const " + i
  else:
    final += i
  if ("(" in i) or ("<<" in i) or ("return" in i):
    if (not i.endswith("{")):
      final += ";"
  final += "\n"
final = final.replace("<<", "=")
final = final.replace("(g_print)", "g_print")
final = """
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
""" + final
f = open("g_index.js", "w")
f.write(final)
f.close()
print("Succesfully compiled `"+filename+"`. ")
