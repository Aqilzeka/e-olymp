Program KNumbers;
var TZ,Z,NZ:Longint;
    N,K:Byte;
procedure Try(I:Byte; var TZ,Z,NZ:Longint);
var  OTZ,OZ,ONZ:Longint;
begin
  if I=1
      then
        begin
          TZ:=0;Z:=0;NZ:=K-1;
        end
      else
        begin
          Try(I-1,OTZ,OZ,ONZ);
          TZ:=OTZ*K+Z;
          Z:=ONZ;
          NZ:=OZ*(K-1)+ONZ*(K-1);
        end
end;


begin
  Readln(N,K);
  Try(N,TZ,Z,NZ);
  Writeln(Z+NZ);
end.
