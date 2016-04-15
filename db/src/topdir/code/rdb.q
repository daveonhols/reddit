args:.Q.opt .z.x;
src:`$first args`source;
upd:insert;
upd:{[t;d] tt::t; dd::d; insert[t;d]}
hsrc:hopen src
startup:hsrc({ .u.sub[]; (tplog;{(x;0#value x)}each tables `.) };0);
{ .[x;();:;y] }./:last startup;
-11!first startup;
