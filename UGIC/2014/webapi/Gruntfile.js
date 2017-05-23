/* jshint camelcase:false */
module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            files: [
                '*.html'
            ],
            options: {
                livereload: true
            }
        },
        connect: {
            uses_defaults: {}
        }
    });

    // Register tasks.
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Default task.
    grunt.registerTask('default', ['connect', 'watch']);
};