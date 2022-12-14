## Домашнее задание к занятию «2.4. Инструменты Git»
### 1. Найдите полный хеш и комментарий коммита, хеш которого начинается на aefea. 

***Решение 1: Выполнил команд git log -p, после в выданном результате, через "/" (поиск) ввел aefea или командой git log -p | grep aefea (в linux)***

***Решение 2: Выполнил команду git show aefea***

commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
Date:   Thu Jun 18 10:29:58 2020 -0400

Update CHANGELOG.md

diff --git a/CHANGELOG.md b/CHANGELOG.md
index 86d70e3e0d..588d807b17 100644
--- a/CHANGELOG.md
+++ b/CHANGELOG.md
@@ -27,6 +27,7 @@ BUG FIXES:
 * backend/s3: Prefer AWS shared configuration over EC2 metadata credentials by default ([#25134](https://github.com/hashicorp/terraform/issues/25134))
 * backend/s3: Prefer ECS credentials over EC2 metadata credentials by default ([#25134](https://github.com/hashicorp/terraform/issues/25134))
 * backend/s3: Remove hardcoded AWS Provider messaging ([#25134](https://github.com/hashicorp/terraform/issues/25134))
+* command: Fix bug with global `-v`/`-version`/`--version` flags introduced in 0.13.0beta2 [GH-25277]
 * command/0.13upgrade: Fix `0.13upgrade` usage help text to include options ([#25127](https://github.com/hashicorp/terraform/issues/25127))
 * command/0.13upgrade: Do not add source for builtin provider ([#25215](https://github.com/hashicorp/terraform/issues/25215))
 * command/apply: Fix bug which caused Terraform to silently exit on Windows when using absolute plan path ([#25233](https://github.com/hashicorp/terraform/issues/25233))

### 2.  Какому тегу соответствует коммит 85024d3?

***Решение 1: git log 85024d3***

commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)
Author: tf-release-bot <terraform@hashicorp.com>
Date:   Thu Mar 5 20:56:10 2020 +0000

    v0.12.23

***Решение 2: Выполнил команду git show 85024d3***

commit 85024d3100126de36331c6982bfaac02cdab9e76 (tag: v0.12.23)  
Author: tf-release-bot <terraform@hashicorp.com>  
Date:   Thu Mar 5 20:56:10 2020 +0000  

    v0.12.23

diff --git a/CHANGELOG.md b/CHANGELOG.md  
index 1a9dcd0f9b..faedc8bf4e 100644  
--- a/CHANGELOG.md  
+++ b/CHANGELOG.md  
@@ -1,4 +1,4 @@  
-## 0.12.23 (Unreleased)  
+## 0.12.23 (March 05, 2020)  
 ##0.12.22 (March 05, 2020)  
  
 ENHANCEMENTS:  
diff --git a/version/version.go b/version/version.go    
index 33ac86f5dd..bcb6394d2e 100644    
--- a/version/version.go    
+++ b/version/version.go    
@@ -16,7 +16,7 @@ var Version = "0.12.23"    
 // A pre-release marker for the version. If this is "" (empty string)    
 // then it means that it is a final release. Otherwise, this is a pre-release    
 // such as "dev" (in development), "beta", "rc1", etc.  
-var Prerelease = "dev"  
+var Prerelease = ""  
  
 // SemVer is an instance of version.Version. This has the secondary    
 // benefit of verifying during tests and init time that our version is a    
 
### 3. Сколько родителей у коммита b8d720? Напишите их хеши.

***Решение 1: Выполнил команду git show b8d720 (родителе в разделе MERGE:)***

commit b8d720f8340221f2146e4e4870bf2ee0bc48f2d5
Merge: 56cd7859e0 9ea88f22fc
Author: Chris Griggs <cgriggs@hashicorp.com>
Date:   Tue Jan 21 17:45:48 2020 -0800

   Merge pull request #23916 from hashicorp/cgriggs01-stable

[Cherrypick] community links

***Решение 2: Выполнил команду git rev-list --parents -n 1 b8d720***

b8d720f8340221f2146e4e4870bf2ee0bc48f2d5 56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b

P.s. Сам коммит, затем родитель 1, затем родитель 2

***Решение 3: Выполнить команду git log --pretty=%P -n 1  b8d720***

56cd7859e05c36c06b56d013b55a252d0bb7e158 9ea88f22fc6269854151c571162c5bcf958bee2b

### 4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами v0.12.23 и v0.12.24.

***Выполнить командру git log  v0.12.23...v0.12.24  --oneline***

33ff1c03bb (tag: v0.12.24) v0.12.24  
b14b74c493 [Website] vmc provider links  
3f235065b9 Update CHANGELOG.md  
6ae64e247b registry: Fix panic when server is unreachable  
5c619ca1ba website: Remove links to the getting started guide's old location  
06275647e2 Update CHANGELOG.md  
d5f9411f51 command: Fix bug when using terraform login on Windows  
4b6d06cc5d Update CHANGELOG.md  
dd01a35078 Update CHANGELOG.md  
225466bc3e Cleanup after v0.12.23 release  

>P.S. Прочел в подсказках, можно сделать командой:  
> git log v0.12.24 -11 --oneline  
33ff1c03bb (tag: v0.12.24) v0.12.24  
b14b74c493 [Website] vmc provider links  
3f235065b9 Update CHANGELOG.md  
6ae64e247b registry: Fix panic when server is unreachable  
5c619ca1ba website: Remove links to the getting started guide's old location  
06275647e2 Update CHANGELOG.md  
d5f9411f51 command: Fix bug when using terraform login on Windows  
4b6d06cc5d Update CHANGELOG.md  
dd01a35078 Update CHANGELOG.md  
225466bc3e Cleanup after v0.12.23 release  
85024d3100 (tag: v0.12.23) v0.12.23  
>>Хотя скорее так деаль неверно, я же не знаю заранее сколько строк (коммитов) прошло с момента от (tag: v0.12.24) и до (tag: v0.12.23)

### 5. Найдите коммит в котором была создана функция func providerSource, ее определение в коде выглядит так func providerSource(...) (вместо троеточего перечислены аргументы).

***Выполнить команду git log -S "func providerSource" --oneline***

5af1e6234a main: Honor explicit provider_installation CLI config when present  
8c928e8358 main: Consult local directories as potential mirrors of providers

***После командо git show просмотрел коммиты и нашел в котором добавляется функция***

commit 8c928e83589d90a031f811fae52a81be7153e82f

### 6. Найдите все коммиты в которых была изменена функция globalPluginDirs.

***Сначала сделал так: Выполнить команду git log -S "globalPluginDirs" --oneline***

125eb51dc4 Remove accidentally-committed binary
22c121df86 Bump compatibility version to 1.3.0 for terraform core release (#30988)
35a058fb3d main: configure credentials from the CLI config file
c0b1761096 prevent log output during init
8364383c35 Push plugin discovery down into command package

Но результат был другой! или я путаюсь.

***ИЛИ Потом делал так: git grep globalPluginDirs***

commands.go:            GlobalPluginDirs: globalPluginDirs(),  
commands.go:    helperPlugins := pluginDiscovery.FindPlugins("credentials", globalPluginDirs())  
internal/command/cliconfig/config_unix.go:              // FIXME: homeDir gets called from globalPluginDirs during init, before  
plugins.go:// globalPluginDirs returns directories that should be searched for  
plugins.go:func globalPluginDirs() []string {   

***затем искать в каждом файле через git log -L :globalPluginDirs:plugins.go и глазами смотреть изменения***

### 7. Кто автор функции synchronizedWriters?

***Выполнить команду git log -S "func synchronizedWriters" --pretty=format:'%h - %an %ae'***

bdfea50cc8 - James Bardin j.bardin@gmail.com  
5ac311e2a9 - Martin Atkins mart@degeneration.co.uk  

git show для просмотра коммитов

commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5   
Author: Martin Atkins <mart@degeneration.co.uk>   
Date:   Wed May 3 16:25:41 2017 -0700   


  

