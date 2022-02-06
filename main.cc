#include <QCoreApplication>
#include <fmt/core.h>
#include <iostream>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <spdlog/sinks/stdout_color_sinks.h>
#include <spdlog/spdlog.h>

int main(int argc, char *argv[]) {
  auto console = spdlog::stdout_color_mt("console");
  QCoreApplication a(argc, argv);
  cv::Mat image;
  std::string picturePath{"vlc.png"};
  image = cv::imread(picturePath, 1);

  if (!image.data) {
    console->info("打开图片失败: {}", picturePath);
    return 0;
  }

  cv::Mat roi = image(cv::Rect(100, 100, 300, 300));
  cv::Mat color(roi.size(), CV_8UC3, cv::Scalar(0, 125, 125));
  double alpha = 0.3;
  cv::addWeighted(color, alpha, roi, 1.0 - alpha, 0.0, roi);
  cv::namedWindow("Display Image", cv::WINDOW_AUTOSIZE);
  cv::imshow("Display Image", image);
  console->info("cv wait key");
  cv::waitKey(0);
  console->info("app.exec");
  return a.exec();

  // return a.exec();
}
