angular.module('todo', [])
  .controller('TaskCtrl', ['$scope', '$http', function($scope, $http) {

  	$http.get('/todo/api/v1.0/tasks')
  		.success(function(response) {
  			console.log(response);
  			$scope.todolist = response.tasks;
  		});

    $scope.delete = function(id) {

      $http.delete('/todo/api/v1.0/tasks/' + id)
        .success(function(response) {
          console.log(response);
          $scope.todolist = response.tasks;
        });

    }  	

  	$scope.register = function() {
  		
  		var task = {
  			title : $scope._title,
  		  description : $scope._description
  		}

  		$http.post('/todo/api/v1.0/tasks', task)
  			.success(function(response) {
          console.log(response);
          $scope.todolist = response.tasks;
  			});
  	}

  }]);