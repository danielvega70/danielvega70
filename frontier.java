import org.ros.node.ConnectedNode;
import org.ros.node.topic.Subscriber;
import org.ros.node.topic.Publisher;
import org.ros.message.MessageListener;
import org.ros.message.MessageFactory;
import org.ros.message.Time;
import org.ros.node.Node;
import org.ros.namespace.GraphName;
import org.ros.exception.RosException;
import sensor_msgs.LaserScan;
import geometry_msgs.Twist;

import java.util.Stack;

public class FrontierExplorer {

    private ConnectedNode node;
    private Publisher<Twist> cmdVelPub;
    private LaserScan laserMsg;
    private float[] laserRanges;
    private boolean laserReceived = false;

    public FrontierExplorer(ConnectedNode connectedNode) {
        this.node = connectedNode;

        // Subscribe to the laser scan topic
        Subscriber<LaserScan> laserSub = connectedNode.newSubscriber("/scan", LaserScan._TYPE);
        laserSub.addMessageListener(new MessageListener<LaserScan>() {
            @Override
            public void onNewMessage(LaserScan message) {
                laserMsg = message;
                laserRanges = message.getRanges();
                laserReceived = true;
            }
        });

        // Create a publisher for the cmd_vel topic
        cmdVelPub = connectedNode.newPublisher("/cmd_vel", Twist._TYPE);

        // Start the DFS algorithm
        new Thread(new Runnable() {
            @Override
            public void run() {
                while (!laserReceived) {
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }

                DFS();
            }
        }).start();
    }

    // Define the DFS algorithm
    private void DFS() {
        // Create a stack to keep track of the visited nodes
        Stack<int[]> nodeStack = new Stack<>();

        // Create a 2D array to keep track of the visited nodes
        int[][] visited = new int[laserMsg.getRanges().length][laserMsg.getRanges().length];

        // Set the starting position to the middle of the environment
        int x = laserMsg.getRanges().length / 2;
        int y = laserMsg.getRanges().length / 2;

        // Push the starting position onto the stack
        nodeStack.push(new int[] {x, y});

        // Loop until the stack is empty
        while (!nodeStack.empty()) {
            // Get the current position
            int[] currentNode = nodeStack.pop();

            // Check if the current node is a frontier
            if (laserRanges[currentNode[0] + currentNode[1] * laserMsg.getRanges().length] > 3.0 && visited[currentNode[0]][currentNode[1]] == 0) {
                // Publish a command to move to the frontier
                Twist cmdVelMsg = cmdVelPub.newMessage();
                cmdVelMsg.getLinear().setX(0.5);
                cmdVelPub.publish(cmdVelMsg);

                // Mark the frontier as visited
                visited[currentNode[0]][currentNode[1]] = 1;
            } else {
                // Mark the current node as visited
                visited[currentNode[0]][currentNode[1]] = 1;

                // Push the neighbors onto the stack
                if (currentNode[0] > 0 && visited[currentNode[0] - 1][currentNode[1]] == 0) {
                    nodeStack.push(new int[] {currentNode[0] - 1, currentNode[1]});
                }
                if (currentNode[0]
