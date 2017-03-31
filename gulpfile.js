'use strict';

var gulp = require("gulp"),
    del = require('del'),
    rename = require("gulp-rename"),
    sourcemaps = require('gulp-sourcemaps'),
    watch = require('gulp-watch');

var pathToBackup = '../remove-more-backup';



gulp.task('backup', function(){
    return gulp.src(['**/*', '!**/*.py___jb_tmp___'])
        .pipe(gulp.dest(pathToBackup))
})
gulp.task('watch', function() {
  gulp.watch('**/*',
  ['backup']);
});
gulp.task('default', ['backup'], function() {
  gulp.start('watch');
});