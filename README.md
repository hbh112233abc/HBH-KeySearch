# HBH-KeySearch
> a sublime text3 plugin for keywords search at browser search driver.

## How setting
```
    {
        "default_driver":"baidu",
        "search_format":{
            "baidu":"https://www.baidu.com/s?wd={key}",
            "360":"https://www.so.com/s?q={key}",
            "bing":"https://cn.bing.com/search?q={key}",
            "google":"https://www.google.com.hk/search?q={key}"
        }
    }
```
> please set keywords *{key}*

## How use
1. `Ctrl+Alt+k` search the selected keywords with default driver;
2. mouse right click call context menu,select `HBH-KeySearch`;
3. after step1 or step2,browser will running and open the search driver to search the result of the selected keywords.

