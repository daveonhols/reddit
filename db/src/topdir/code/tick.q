/ hclose loghandle
\l code/reddit.q
tplog:`$":./tplog/",string .z.d;
if[()~key tplog;.[tplog;();:;()]];
loghandle:hopen tplog;

subscriber:0N;

.u.upd:{[tbl;data]
    if[not 19h=abs type first data;data:(enlist enlist .z.t),enlist each data];
    msg:(`upd;tbl;data);
    loghandle @ enlist  msg;
    .u.pub[tbl;data];
  };

.u.pub:{[tbl;data]
    if[null subscriber;:()];
    (neg subscriber) @ (`upd;tbl;data)
  };

.u.sub:{[]
    `subscriber set .z.w;
  };

.z.pc:{[handle]
    show "gone away: ",-3!handle;
    if[handle=subscriber;`subscriber set 0N];
  };

