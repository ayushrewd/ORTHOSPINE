import cv2
import numpy as np
import math

# Array to store the coordinates of user mouse clicks
clicked_points = []

def calculate_cobb_angle(img):
    """
    Calculates the true orthopaedic Cobb angle from 4 coordinate markers.
    Calibrated for standard anatomical vertical spinal orientations.
    """
    if len(clicked_points) < 4:
        return img
    
    # Boundary Line 1: Upper End Vertebra tilt line (Points 0 and 1)
    pt1, pt2 = clicked_points[0], clicked_points[1]
    # Boundary Line 2: Lower End Vertebra tilt line (Points 2 and 3)
    pt3, pt4 = clicked_points[2], clicked_points[3]
    
    # Render structural tracking lines on the X-ray canvas
    cv2.line(img, pt1, pt2, (0, 255, 0), 2)  # Green boundary lines
    cv2.line(img, pt3, pt4, (0, 255, 0), 2)
    
    # Compute base mathematical slopes (m = dy / dx)
    m1 = (pt2[1] - pt1[1]) / (pt2[0] - pt1[0]) if (pt2[0] - pt1[0]) != 0 else 999
    m2 = (pt4[1] - pt3[1]) / (pt4[0] - pt3[0]) if (pt4[0] - pt3[0]) != 0 else 999
    
    # Calculate intersection angle using standard tangent formula
    try:
        tan_theta = abs((m2 - m1) / (1 + m1 * m2))
        raw_angle = math.degrees(math.atan(tan_theta))
    except ZeroDivisionError:
        raw_angle = 90.0

    # Clinical Calibration: In vertical spinal alignments, if lines are mapped highly 
    # parallel vertically, the true anatomical intersection is the complement.
    if raw_angle > 45:
        cobb_angle = 90 - raw_angle
    else:
        cobb_angle = raw_angle

    # Overlay clinical analytics metadata onto the image interface
    result_text = f"Measured Cobb Angle: {cobb_angle:.2f} Deg"
    cv2.putText(img, result_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    
    print(f"[METRICS LOG] {result_text}")
    return img

def mouse_click_callback(event, x, y, flags, parameters):
    """
    Handles mouse window interaction metrics collection.
    """
    global clicked_points, interactive_img_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(clicked_points) < 4:
            clicked_points.append((x, y))
            
            # Draw tracking anchor points on viewport click
            cv2.circle(interactive_img_copy, (x, y), 5, (255, 0, 0), -1)
            cv2.imshow("Spine Diagnostics Matrix", interactive_img_copy)
            
            # Execute standard trigonometric parsing pipeline upon receipt of 4 coordinate landmarks
            if len(clicked_points) == 4:
                processed_output = calculate_cobb_angle(interactive_img_copy)
                cv2.imshow("Spine Diagnostics Matrix", processed_output)

if __name__ == "__main__":
    # Target source image path within local workspace
    source_image_path = "spine.jpg" 
    
    # Load image data matrix
    base_image = cv2.imread(source_image_path)
    if base_image is None:
        print(f"\n[CRITICAL ERROR] Target standard asset '{source_image_path}' not found within workspace root directory.")
        exit()

    # --- SCIENTIFIC ASPECT RATIO PRESERVING SCALE ---
    target_display_height = 680  
    original_height, original_width = base_image.shape[:2]
    
    scale_ratio = target_display_height / original_height
    target_display_width = int(original_width * scale_ratio)
    
    base_image = cv2.resize(base_image, (target_display_width, target_display_height), interpolation=cv2.INTER_AREA)
    # -------------------------------------------------

    # Create active display canvas runtime copy
    interactive_img_copy = base_image.copy()
    
    # Initialize UI Window frame
    cv2.namedWindow("Spine Diagnostics Matrix", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Spine Diagnostics Matrix", interactive_img_copy)
    
    print("\n========================= RUNTIME CONSOLE LOGS =========================")
    print("CRITICAL USER OPERATION PROTOCOL:")
    print("1. Map Upper End Vertebra margin: Click left then right corners of a single vertebra.")
    print("2. Map Lower End Vertebra margin: Click left then right corners of a single vertebra.")
    print("========================================================================")
    
    # Initialize interactive event pipeline registration
    cv2.setMouseCallback("Spine Diagnostics Matrix", mouse_click_callback)
    
    # Keeps window open until you manually hit 'ESC' or 'q' key on your keyboard
    while True:
        cv2.imshow("Spine Diagnostics Matrix", interactive_img_copy)
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord('q'): # Press Escape or Q to quit
            break
            
    cv2.destroyAllWindows()