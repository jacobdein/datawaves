/**
 *
 *  gulpfile for signalin
 *  Copyright 2016. All rights reserved.
 *
 *
 *
 */

'use strict';

// Include gulp and required plug-ins
var gulp = require('gulp');
var browserSync = require('browser-sync');
var concat = require('gulp-concat');
var compass = require('gulp-compass');
var del = require('del');
//var exec = require('gulp-exec');
var exec = require('child_process').exec;
var gulpif = require('gulp-if');
var gutil = require('gulp-util');
var imagemin = require('gulp-imagemin');
var minifyCSS = require('gulp-minify-css');
var minifyHTML = require('gulp-minify-html');
var pngquant = require('imagemin-pngquant');
var uglify = require('gulp-uglify');

var env, 
	outputDir,
	productionDir, 
	sassStyle, 
	sourceHTML, 
	sourceImages, 
	sourceScripts, 
	sourceStyles;

// environment = development (default) or production
env = process.env.NODE_ENV || 'development';

// source files
sourceHTML = ['client/html/*.html'];
sourceScripts = ['client/scripts/*.js'];
sourceStyles = ['client/styles/style.scss', 'client/styles/elements.scss'];
sourceImages = ['client/images/**/*.jpg', 'client/images/**/*.png', 'client/images/**/*.gif'];

// set production directory
productionDir = 'builds/production/server';

// output build to environment (development or production)
if (env==='production') {
	outputDir = 'builds/production/';
	sassStyle = 'compressed';
}	else {
	outputDir = 'builds/development/';
	sassStyle = 'expanded';
}

// set environment to production
gulp.task('set-production-env', function () {
	env = 'production';
	outputDir = 'builds/production/';
	sassStyle = 'compressed';
});

// process images
gulp.task('images', function () {
	gulp.src(sourceImages)
		.pipe(gulpif(env === 'production', imagemin({
			interlaced: true,
			progressive: true,
			use: [pngquant()]
		})))
		.pipe(gulp.dest(outputDir + 'static/images'))
});

// process scripts
gulp.task('scripts', function() {
	gulp.src(sourceScripts)
		.pipe(concat('script.js'))
		.pipe(gulpif(env === 'production', uglify()))
		.pipe(gulp.dest(outputDir + 'static/scripts'))
		.on('error', gutil.log);
});

// process styles
gulp.task('styles', function() {
	gulp.src(sourceStyles)
		.pipe(compass({
			css: outputDir + 'static/styles',
			sass: 'client/styles',
			style: sassStyle,
			require: ['susy', 'breakpoint']
		}))
		.pipe(gulpif(env === 'production', minifyCSS()))
		.pipe(gulp.dest(outputDir + 'static/styles'))
		.pipe(browserSync.reload({stream:true}))
		.on('error', gutil.log);
});

// process HTML
gulp.task('html', function() {
	gulp.src(sourceHTML)
	.pipe(gulpif(env === 'production', minifyHTML()))
	.pipe(gulp.dest(outputDir + 'static/html'))
	.on('error', gutil.log);
});

// start development server
gulp.task('browser-sync', function() {
	browserSync({
		proxy: 'localhost:8000'
	});
});

// reload development server
gulp.task('reload', function () {
	browserSync.reload();
});

// clean build
gulp.task('clean', function() {
	del(['builds']);
});

// watch files for changes
gulp.task('watch', function() {
	gulp.watch(sourceImages, ['images', 'reload']);
	gulp.watch(sourceHTML, ['html', 'reload']);
	gulp.watch(sourceScripts, ['scripts', 'reload']);
	gulp.watch('client/styles/**/*.scss', ['styles']);
});

// build files without starting server
gulp.task('build', ['images', 'scripts', 'styles', 'html']);

// build files for production
gulp.task('build-production', ['set-production-env', 'images', 'scripts', 'styles', 'html'], function (cb) {
	//copy all django server files
	gulp.src('server/**/*')
		.pipe(gulp.dest(productionDir))
		.on('error', gutil.log);
	// overrite some settings for production environment
/*	exec('python set_production_settings.py', function (err, stdout, stderr) {
		console.log(stdout);
		console.log(stderr);
		cb(err);
	});
	// run django deploy check
	exec('python builds/production/server/manage.py check --deploy', function (err, stdout, stderr) {
		console.log(stdout);
		console.log(stderr);
		cb(err);
	}); */
});

// default task 
gulp.task('default', ['images', 'scripts', 'styles', 'html', 'browser-sync', 'watch']);
