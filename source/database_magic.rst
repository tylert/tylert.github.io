SQLite
------

* https://www.sqlitetutorial.net/sqlite-primary-key
* https://sqlite.org/datatype3.html  primitive datatypes
* https://www.sqlite.org/lang_corefunc.html  built-in functions
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
* https://sqlpkg.org  extensions
* https://github.com/dgllghr/stanchion  column-oriented tables for sqlite
* https://github.com/lovasoa/sqlpage
* https://sql.ophir.dev
* https://github.com/dgllghr/stanchion
* https://github.com/nalgeon/redka  Redis-compatible sqlite
* https://lumosql.org  pluggable backend which supports encryption?
* https://github.com/LMDB/lmdb  might be part of the magic of LumoSQL
* https://syntax.fm/show/779/why-sqlite-is-taking-over-with-brian-holt-and-marco-bambini
* https://github.com/glebarez/go-sqlite  embedded sqlite
* https://oldmoe.blog/2024/04/30/backup-strategies-for-sqlite-in-production
* https://highperformancesqlite.com
* https://bedrockdb.com
* https://github.com/Expensify/Bedrock
* https://speakerdeck.com/fractaledmind/how-and-why-to-run-sqlite-in-production
* https://blog.pecar.me/sqlite-prod
* https://turso.tech
* https://www.reddit.com/r/rails/comments/k4vlqo/is_anyone_using_sqlite_on_production_either_side
* https://wafris.org/blog/rearchitecting-for-sqlite
* https://starbasedb.com/blog/building-an-http-sqlite-database-with-cloudflare-durable-objects
* https://starbasedb.com/blog/developing-acid-transaction-support-in-starbasedb
* https://stackoverflow.com/questions/6076984/sqlite-how-do-i-save-the-result-of-a-query-as-a-csv-file
* https://mrsuh.com/articles/2024/sqlite-index-visualization-structure
* https://stackoverflow.com/questions/2359205/copying-data-from-one-sqlite-database-to-another
* https://turso.tech/blog/introducing-limbo-a-complete-rewrite-of-sqlite-in-rust
* https://misfra.me/2025/virtual-tables-in-sqlite-with-go
* https://misfra.me/2025/sqlite-transactions-and-virtual-tables

::

    sqlite3 foo.sqlite3 .dump > foo.sql

UUID stuff::

    -- help doc at https://sqlite.org/loadext.html
    -- "raw" src file from https://sqlite.org/src/file/ext/misc/uuid.c
    -- gcc -g -fPIC -shared uuid.c -o uuid.so
    .load ./uuid
    CREATE TABLE foo (id UUID PRIMARY KEY, name TEXT);
    INSERT INTO foo VALUES (uuid(), 'udders');


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
* https://kubeblocks.io  databases in k8s


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
* https://sqlsync.dev  eventually-consistent SQLite, offline-first
* https://github.com/orbitinghail/sqlsync
* https://rivet.gg/blog/2025-02-16-sqlite-on-the-server-is-misunderstood


Indexing
--------

* https://blog.scaledcode.com/blog/analyzing-new-unique-id
* https://github.com/asg017/sqlite-ulid
* https://github.com/ulid/spec
* https://github.com/nalgeon/sqlean  ultimate sqlite extension pack?


Querying
--------

* https://github.com/TomWright/dasel  CSV, JSON, TOML, XML, YAML data management? (Golang)
* https://github.com/YS-L/csvlens  like less but for CSV?
* https://matthodges.com/posts/2024-08-12-csv-bad-dsv-good
* https://github.com/archiewood/gosql
* https://simonwillison.net/2024/Nov/25/ask-questions-of-sqlite
* https://github.com/medialab/xan  the CSV magician
* https://github.com/cube2222/octosql  CLI tool to join JSON with SQL and other weird things


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
* https://kaveland.no/friends-dont-let-friends-export-to-csv.html
* https://blog.ploeh.dk/2024/06/03/youll-regret-using-natural-keys
* https://gobuffalo.io  CRUD magic
* https://github.com/gobuffalo/pop  CRUD magic
* https://karmanivero.us/projects/entity-manager/evolving-a-nosql-db-schema
* https://github.com/sqlalchemy/sqlalchemy/wiki/SchemaDisplay
* https://github.com/eralchemy/eralchemy
* https://stackoverflow.com/questions/44981986/sqlalchemy-er-diagram-in-python-3
* https://github.com/kaishuu0123/erd-go  ER diagrams from text using Graphviz
* https://typst.app/universe/package/pintorita
* https://github.com/taylorh140/typst-pintora  Pintorita plugin for Typst
* https://pintorajs.vercel.app/docs/intro


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
* https://tinybase.org  apparently, plays well with SQLite (local-first data)
* https://github.com/tinyplex/tinybase  TinyBase (Jabbascript)
* https://www.viblo.se/posts/no-need-redis  maybe you don't need Redis
* https://github.com/sebadob/hiqlite


PostgreSQL
----------

* https://layerci.com/blog/postgres-is-the-answer
* https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb  PostgreSQL is "enough"
* https://www.amazingcto.com/postgres-for-everything
* https://github.com/tembo-io/pgmq  AWS SQS clone for PostgreSQL
* https://github.com/omnigres/omnigres
* https://docs.omnigres.org
* https://tembo.io/blog/pg-timeseries
* https://github.com/kiwicopple/serverless-postgres
* https://www.orioledb.com
* https://github.com/zalando/spilo  HA containerized PostgreSQL cluster thingy
* https://event-driven-io.github.io/Pongo  mongodb without mongodb?
* https://github.com/event-driven-io/Pongo
* https://github.com/janbjorge/PgQueuer  PostreSQL as a queue
* https://xata.io/blog/postgres-webhooks-with-pgstream
* https://challahscript.com/what_i_wish_someone_told_me_about_postgres
* https://github.com/frectonz/pglite-fusion  SQLite databases in PostgreSQL tables


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

* https://github.com/dolthub/go-mysql-server


SlateDB
-------

* https://slatedb.io  database in S3???
* https://github.com/slatedb/slatedb/issues/164  remove the need for DynamoDB in order to run SlateDB???
* https://github.com/slatedb/slatedb
* https://github.com/slatedb/slatedb-go


Datalakes
---------

* https://ludic.mataroa.blog/blog/get-me-out-of-data-hell
