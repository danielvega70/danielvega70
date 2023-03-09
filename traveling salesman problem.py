from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def create_data_model():
    """Stores the data for the problem."""
    data = {}
    # Define the distance matrix between cities
    data['distance_matrix'] = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Define the number of cities
    data['num_cities'] = 4
    # Define the starting city
    data['depot'] = 0
    return data

def print_solution(manager, routing, assignment):
    """Prints the solution."""
    # Get the total travel distance
    print(f"Total distance: {assignment.ObjectiveValue()} miles\n")
    # Get the route for each vehicle
    for vehicle_id in range(routing.GetVehicleCount()):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        route_distance = 0
        while not routing.IsEnd(index):
            # Get the name of the current city
            plan_output += f" {manager.IndexToNode(index)} ->"
            # Add the distance to the total travel distance
            previous_index = index
            index = assignment.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        # Add the distance from the last city to the starting city to complete the loop
        plan_output += f" {manager.IndexToNode(index)}\n"
        route_distance += routing.GetArcCostForVehicle(previous_index, routing.Start(vehicle_id), vehicle_id)
        plan_output += f"Distance of route {vehicle_id}: {route_distance} miles\n"
        print(plan_output)

def main():
    """Solve the Traveling Salesman Problem."""
    # Create the data model
    data = create_data_model()
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(data['num_cities'], 1, data['depot'])
    # Create the routing model
    routing = pywrapcp.RoutingModel(manager)
    # Define the distance callback
    def distance_callback(from_index, to_index):
        """Returns the distance between two cities."""
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]
    # Register the distance callback
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    # Define the distance cost function
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    # Define the search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    # Solve the problem
    assignment = routing.SolveWithParameters(search_parameters)
    # Print the solution
    if assignment:
        print_solution(manager, routing, assignment)

if __name__ == '__main__':
    main()
