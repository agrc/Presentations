A Few of our Favorite Things
============================
2015 ESRI Dev Summit Abstract

Within the last few years, front-end development tooling has made major strides. It seems that everyday we discover (or create) a new tool and think to ourselves, "How did we live without this"? This presentation will outline just a few of our favorite tools that make our lives easier such as [`grunt-esri-slurp`](https://github.com/steveoh/grunt-esri-slurp), [`amd-butler`](https://github.com/agrc/AmdButler), [`travis-ci`](https://travis-ci.org/), [`sauce-labs`](https://saucelabs.com/), [`bower`](http://bower.io/) and others.

Come and see how AGRC wires these technologies together to enable rapid development while improving code quality.


### Outline

intro (Scott) | 1 min
- Names and AGRC
- outline of presentation

bower (Steve) | 2 min
- We use bower to manage all of our front end dependencies
- show deps for deq-enviro
- Wouldn't it be nice if we could bower install esri?

grunt-esri-slurp (Scott) | 5 min
- As close as you can get to bower install esri
- http://gis.utah.gov/grunt-esri-slurp/
- build system, debugging, travis

AMD Butler (Steve) | 5 min
- show adding modules by hand
- sorting
- adding
- removing
- highlight esri modules and how grunt-esri-slurp made this possible

travis-ci (Scott/Steve) | 4 min
- show .travis.yml
- performance tip: container based architecture
- show how grunt-esri-slurp makes it possible to run tests and do a build
- build status on PR pages to prevent the merging of bad PR's
- mention saucelabs

grunt-arcgis-press (Scott/Steve) | 3 min
- preview