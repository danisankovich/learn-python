function age(year,month,day){
  var input = new Date(year,month,day);
  var now = Date.now();
  var diffdays = Math.floor(Math.abs(now-input)/1000/3600/24);
  if (diffdays<365&&diffdays>30){
    return Math.floor(diffdays/30)+" months "+diffdays%30+" days";
  }
  else if(diffdays>365){
    return Math.floor(diffdays/365)+" years "+Math.floor((diffdays%365)/30)+" months "+diffdays%30+" days";
  }
  else{return diffdays+" days";}
}
console.log(age(2016, 0, 12));
