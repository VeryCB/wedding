var gulp = require('gulp');
var minify = require('gulp-minify-css');

var cssFiles = 'mario/src/css/*.css';

gulp.task('minify', function() {
    gulp.src(cssFiles)
        .pipe(minify({
            keepBreaks: true
        }))
        .pipe(gulp.dest('mario/static/css/'));
});

gulp.task('watch', function () {
    gulp.watch(cssFiles, [minify]);
});

gulp.task('default', ['minify']);
