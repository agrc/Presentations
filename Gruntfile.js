/* jshint camelcase:false */
module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        watch: {
            files: [
                '**/*.html',
                '**/*.css'
            ],
            options: {
                livereload: true
            }
        },
        connect: {
            uses_defaults: {}
        },
        'gh-pages': {
            src: ['favorite-things/**',
                'web-application-options/**']
        }
    });

    // Register tasks.
    grunt.loadNpmTasks('grunt-contrib-connect');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-gh-pages');

    // Default task.
    grunt.registerTask('default', ['connect', 'watch']);
    grunt.registerTask('publish', ['gh-pages'])
};
