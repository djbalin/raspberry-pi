#!/bin/bash

# Simple Background Python Runner Script
# Usage: runbg.sh <python_file> [output_directory]

if [ $# -eq 0 ]; then
    echo "Usage: $0 <python_file> [output_directory]"
    echo "Example: $0 ens160.py"
    echo "Example: $0 ens160.py /path/to/logs"
    echo ""
    echo "Default output directory: ./output/"
    exit 1
fi

PYTHON_FILE="$1"
OUTPUT_DIR="${2:-./output}"

# Check if Python file exists
if [ ! -f "$PYTHON_FILE" ]; then
    echo "Error: Python file '$PYTHON_FILE' not found!"
    exit 1
fi

# Create output directory if it doesn't exist
if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Creating output directory: $OUTPUT_DIR"
    mkdir -p "$OUTPUT_DIR"
fi

# Generate file paths
BASENAME=$(basename "$PYTHON_FILE" .py)
LOG_FILE="$OUTPUT_DIR/${BASENAME}.log"
PID_FILE="$OUTPUT_DIR/${BASENAME}.pid"

# Run the command with system Python
echo "Starting $PYTHON_FILE in background..."
echo "Log file: $LOG_FILE"
echo "PID file: $PID_FILE"
echo ""

nohup python3 "$PYTHON_FILE" > "$LOG_FILE" 2>&1 &
PID=$!

# Save PID to file
echo $PID > "$PID_FILE"

echo "✅ Background process started successfully!"
echo "   Process ID: $PID"
echo "   Monitor output: tail -f $LOG_FILE"
echo "   Stop process: kill $PID"
echo "   Or use: kill \$(cat $PID_FILE)"
echo ""
echo "Output directory contents:"
ls -la "$OUTPUT_DIR" | grep -E "${BASENAME}\.(log|pid)$" 2>/dev/null || echo "   (Log and PID files will appear here)"