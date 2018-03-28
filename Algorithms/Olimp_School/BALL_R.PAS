Program Ball;
var N:integer;
    D:array [1..30] of longint;

Function F(X:integer):longint;
begin
 if D[X]=0 then D[X]:=F(x-1)+F(x-2)+F(x-3);
 F:=D[X]
end;

begin
 for N:=1 to 30 do D[N]:=0;
 D[1]:=1;D[2]:=2;D[3]:=4;
 Readln(N);
 writeln(F(N))
end.
