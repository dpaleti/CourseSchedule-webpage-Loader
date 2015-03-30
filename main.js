//setup app and name it myApp, call ngRoute for routing
var app = angular.module('myApp', ['ngRoute', 'ui.bootstrap']);

function CollapseDemoCtrl($scope) {
    $scope.isCollapsed = true;
}

//setup routing to partials (i.e. the views)
app.config(function ($routeProvider) {
	$routeProvider

	    .when('/',
		  {
		      controller: 'MyCtrl',
		      templateUrl: 'partials/v1.html'
		  })
	    .otherwise({ redirectTo: '/' });

    });


//controller for view 1, the main table
app.controller('MyCtrl', function($scope, $route, $routeParams, dataService) {
	dataService.getData().then(function(data) {
		$scope.myData = data;
	    });
	$scope.$route = $route;
	$scope.$routeParams = $routeParams;
    });

//Factory to get arch.json file and parse it
app.factory('dataService',function($http){
	return {
	    getData: function(){
		return $http.get('js/main.json').then(function(result){
			//clean the data
			var fin = {};
			var finale = [];
			
			angular.forEach(result.data, function(val, key){
				var session = (val.SubtermCode) ? val.SubtermCode : (val.Course).slice(9);
				session = (val.sess) ? val.sess : session;
				
				var max = (val.MaxSize === '999') ? session : session.concat(" / Max ", val.MaxSize);
				
				var clink = val.Term.concat(val.Course);
				var bwlink = ((val.Course).slice(4,8)).concat("-20151-",(val.Course).slice(9));

				var digit1 = (val.NumFixedUnits).charAt(1);
				var pts = (val.NumFixedUnits).charAt(2);
				var pts2 = (pts === '5') ? digit1.concat(".",pts) : digit1 ;

				var cname = (val.Course).slice(0,4);
				var cname2 = "A";
				if (cname === "PLAN")
				    cname2 = cname.slice(0,3);
			      

				fin[val.Course] = {Course: cname2 + (val.Course).slice(4,8),
						   Title: val.CourseTitle, 
						   Instructor: (val.Instructor1Name).split(',')[0],
						   Sess: max,
						   Time: (val.Meets1).slice(0,20),
						   Points: pts2,
						   Location: (val.Meets2).toLowerCase(),
						   Call: val.CallNumber,
						   Enrolled: val.NumEnrolled,
						   Notes: (val.ClassNotes),
						   SchoolCode: (val.Course).slice(0,4),//val.SchoolCode,
						   cwlink: clink,
						   blink: bwlink,
						   Req: val.req,
						   type: val.type,
						   Syllabi: val.syllabi,
						   images: val.images,
						   facsyl: val.facsyl
 
				};
			    });
			angular.forEach(fin, function(v, k){
				finale.push({Course: v.Course, Title: v.Title, Instructor: v.Instructor, Sess: v.Sess,
					    Time: v.Time, Points: v.Points, Location: v.Location, Call: v.Call,
					    Enrolled: v.Enrolled, Notes: v.Notes, SchoolCode: v.SchoolCode,
					    cwlink: v.cwlink, blink: v.blink, Req: v.Req, type: v.type, Syllabi: v.Syllabi, images: v.images, facsyl: v.facsyl
					    });
			    });

			//return json
			return finale;
			
			//return result.data;
		    });
	    }
	}	
    });

app.filter('orderObjectBy', function() {
	return function(items, field, reverse) {
	    var filtered = [];
	    angular.forEach(items, function(item) {
		    filtered.push(item);
		});
	    filtered.sort(function (a, b) {
		    return (a[field] > b[field]);
		});
	    if(reverse) filtered.reverse();
	    return filtered;
	};
    });
