Program robot;
Type T1=array [-16..16,-16..16] of longint;
     T2=array [0..16] of ^T1;
Var X,Y,K,i,j,z:shortint;s:longint;
    D:T2;

Function F(X,Y,Z:integer):longint;
var s:longint;
begin
 if D[Z]^[X,Y]=-1 then
  begin
   s:=0;
   if X<>-16 then s:=s+F(X-1,Y,Z-1);
   if X<>16 then s:=s+F(X+1,Y,Z-1);
   if Y<>-16 then s:=s+F(X,Y-1,Z-1);
   if Y<>16 then s:=s+F(X,Y+1,Z-1);
   D[Z]^[X,Y]:=s;
  end;
 F:=D[Z]^[X,Y];
end;

begin
 for i:=0 to 16 do
  New(D[i]);
 readln(K,X,Y);
 for i:=-16 to 16 do
  for j:=-16 to 16 do
    D[0]^[i,j]:=0;
 D[0]^[0,0]:=1;
 for i:=-16 to 16 do
  for j:=-16 to 16 do
   for z:=1 to 16 do
    D[z]^[i,j]:=-1;
 writeln(F(x,y,k));
 for i:=0 to 16 do
  Dispose(D[i]);
end.