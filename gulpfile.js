'use strict';

var gulp = require("gulp"),
    del = require('del'),
    rename = require("gulp-rename"),
    sourcemaps = require('gulp-sourcemaps'),
    watch = require('gulp-watch');

var pathToBackup = '../remove-more-backup';

function onError(error){
    console.error.bind(error);
}



gulp.task('backup', function(){
    return gulp.src(['**/*'])
        .on('error', onError)
        .pipe(gulp.dest(pathToBackup))

})
gulp.task('watch', function() {
  gulp.watch(['**/*', '!tests/**/*', 'tests/**/*.py', 'tests/**/*.json'],
  ['backup']);
});
gulp.task('default', ['backup'], function() {
  gulp.start('watch');
});