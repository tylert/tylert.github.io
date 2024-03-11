SQLite
------

* https://sqlitebrowser.org
* https://github.com/sqlitebrowser/sqlitebrowser
* https://sqlitestudio.pl
* https://github.com/pawelsalawa/sqlitestudio
* https://til.simonwillison.net/sqlite/one-line-csv-operations  SQL queries on CSV files
* https://simonwillison.net/2021/Feb/21/cross-database-queries  sqlite looking across databases
* https://dba.stackexchange.com/questions/25127/working-with-multiple-databases  more multi-database stuff
* https://stackoverflow.com/questions/80801/how-can-i-merge-many-sqlite-databases  merging
* https://stackoverflow.com/questions/9410011/multiple-files-for-a-single-sqlite-database
* https://github.com/orbitinghail/sqlsync
* https://sqlsync.dev/posts/stop-building-databases
* https://phiresky.github.io/blog/2021/hosting-sqlite-databases-on-github-pages
* https://developers.cloudflare.com/d1/learning/importing-data/#converting-sqlite-database-files
* https://sqlime.org
* https://github.com/nalgeon/sqlime
* https://github.com/dgllghr/stanchion  column-oriented tables for sqlite
* https://github.com/lovasoa/sqlpage
* https://sql.ophir.dev
* https://github.com/dgllghr/stanchion

::

    sqlite3 foo.sqlite3 .dump > foo.sql


JSON
----

* https://www.delphitools.info/2021/06/17/sqlite-as-a-no-sql-database
* https://www.sqlite.org/json1.html
* https://sqlite.org/forum/forumpost/012136abd5292b8d
* https://dgl.cx/2020/06/sqlite-json-support


WAL
---

* https://www.sqlite.org/cgi/src/doc/wal2/doc/wal2.md


Cloud Stuff
-----------

* https://paulbradley.dev/sqlite-efs-serverless-database  AWS serverless sqlite3???


Clustering and Replication
--------------------------

* https://github.com/k3s-io/kine
* https://github.com/maxpert/marmot
* https://maxpert.github.io/marmot
* https://litestream.io
* https://fly.io/blog/introducing-litefs
* https://github.com/superfly/litefs
* https://rqlite.io
* https://github.com/rqlite/rqlite
* https://www.rqlite.com
* https://www.philipotoole.com
* https://dqlite.io
* https://github.com/canonical/dqlite


Indexing
--------

* https://blog.scaledcode.com/blog/analyzing-new-unique-id


Querying
--------

* https://github.com/YS-L/csvlens  like less but for CSV?


Encryption
----------

* https://utelle.github.io/SQLite3MultipleCiphers
* https://github.com/utelle/SQLite3MultipleCiphers


Schema Stuff
------------

* https://blog.turso.tech/database-migrations-made-easy-with-atlas-df2b259862db  terraform-provider-atlas
* https://atlasgo.io  schema management (HCL, SQL, etc.)
* https://atlasgo.io/integrations/terraform-provider
* https://github.com/ariga/atlas
* https://dvc.org/doc/use-cases/data-registry  version control for data?
* https://docs.datasette.io/en/stable/getting_started.html  more data control stuff maybe?


K8s Stuff
---------

* https://youtube.com/watch?v=HycGtLjlikI  Cloud Native Live:  2-node HA for edge Kubernetes - a new approach
* https://operatorframework.io
* https://github.com/glasskube/operator  custom operators?
* https://glasskube.eu


Other Types
-----------

* http://www.sarahmei.com/blog/2013/11/11/why-you-should-never-use-mongodb  careful with MongoDB
* http://blog.wix.engineering/2015/12/10/scaling-to-100m-mysql-is-a-better-nosql
* https://petereliaskraft.net/blog/epoxy  atomic transactions across databases?


PostgreSQL
----------

* https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb  PostgreSQL is "enough"


MySQL Stuff
-----------

::

    select concat('KILL ',id,';') from information_schema.processlist where command='Sleep';

::

    #!/bin/bash

    echo "Killing existing xlsws_category queries"
    for process_id in `mysql -e "show full processlist" | grep 'xlsws_category' | awk '{print $1}'`
    do
        echo "- process: ${process_id}"
        mysql -e "kill ${process_id}"
    done
