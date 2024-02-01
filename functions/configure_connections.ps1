$alembic_file_list = Get-ChildItem -Path $PWD.Path -Recurse -Include alembic.ini -File

$env_path = $PWD.Path + "\.env"
$env_file_content = Get-Content $env_path
$connStr = $env_file_content | Select-String -Pattern "DB_CONNECTION_STRING"
$connStr = $connStr -replace "DB_CONNECTION_STRING=", ""
# change the connection of every alembic.ini file
foreach($alembic_file in $alembic_file_list) {
    $alembic_file_content = Get-Content $alembic_file
    $connection_string_line = $alembic_file_content | Select-String -Pattern "sqlalchemy.url"
    $alembic_file_content = $alembic_file_content -replace "sqlalchemy.url = .*", "sqlalchemy.url = $connStr"
    $alembic_file_content | Set-Content $alembic_file
}