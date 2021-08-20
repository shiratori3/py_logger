# logging 通过yaml配置文件进行配置及其实例化使用

## 配置参数解释

- 详见：[logging.config.html](https://docs.python.org/zh-tw/3/library/logging.config.html)

- disable_existing_loggers: 如果指定为 False，则当执行此调用时已存在的日志记录器会保持启用。 默认值为 True 因为这将以向下兼容方式启用旧行为。 此行为是禁用任何现有的非根日志记录器除非它们或它们的上级在日志记录配置中被显式地命名。

- formatters: 格式器，决定信息的最终输出形式，可配置多个以便不同的处理器进行调用。
  - 样例中配置了三种格式，分别是simple, standard, verbose。

- handlers：处理器，改变信息的输出流，如输出至日志文件或发送邮件至特定地址。
  - 样例中针对每个错误类型各自配置了对应处理，同时设置console以便实时输出信息

- loggers: 记录器，把具体文件与其输出信息等级、处理器联系起来。通过logging.getLogger(name)获取配置文件中对应name的记录器配置。
  - 通过无需每个文件都配置记录器，只需对特定关注的文件配置即可。
  - 一个记录器可以同时有多个处理器
  - propagate指是否传递变量至父级记录器进行进一步处理。

- root：根记录器。在文件未指定记录器（log = logging.getLogger()）的情况下，会调用root根处理器进行处理。

## 使用方法

- 在每个需配置logger的文件夹中导入已实例化的logger即可。不应在每个文件中分别实例化Logger并使用。

- 对于特别关注的文件，可在logging.yaml文件中对其独立设置handlers和loggers。其余文件会默认使用root记录器。

- 样例见bin文件夹的三个template.py文件，其中bin/template.py已配置了独立的记录器，分别运行三个文件可帮助理解Logger的实际运行
