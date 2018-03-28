Program Explosion;
var E,AA,A,B:longint;
    N:byte;
procedure Try(I:Byte; var E,AA,A,B:longint);
var OE,OAA,OA,OB:LongInt;
begin
  if I=0
      then
        begin
          E:=0;AA:=0;A:=0;B:=1
        end
      else
        begin
          Try(I-1,OE,OAA,OA,OB);
          E:=OE*2+OAA;
          AA:=OA;
          A:=OB;
          B:=OAA+OA+OB;
        end

end;


begin
 Readln(N);
 Try(N,E,AA,A,B);
 writeln(E);
end.