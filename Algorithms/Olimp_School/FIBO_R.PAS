Program Fibo;
var I,N:integer;
    D:array [1..50] of longint;

Function F(X:integer):longint;
begin
 if D[X]=0 then
  if (X=1) or (X=2) then D[X]:=1
                    else D[X]:=F(X-1)+F(X-2);
 F:=D[X]
end;

begin
 For N:=1 to 50 do D[N]:=0;
 Readln(N);
 writeln(F(N))
end.