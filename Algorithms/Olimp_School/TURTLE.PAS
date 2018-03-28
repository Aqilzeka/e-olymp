Program Turtle;
var a:array [1..20,1..20] of longint;
    b:array [0..20,0..20] of longint;

Function F(x,y:integer):longint;
begin
 if B[x,y]=-1 then
  if F(x-1,y)>F(x,y-1) then B[x,y]:=F(x-1,y)+A[x,y]
                       else B[x,y]:=F(x,y-1)+A[x,y]
 F:=B[x,y];
end;

var i,j,N:integer;
begin
 Readln(N);
 for i:=1 to N do
  begin
   for j:=1 to N-1 do
    read(A[i,j]);
   readln(A[i,N])
  end;
 for i:=1 to N do
  for j:=1 to N do
   B[i,j]:=-1;
 for i:=0 to N do
  begin
   B[i,0]:=0;
   B[0,j]:=0
  end;
 writeln(F(N,N));
end.