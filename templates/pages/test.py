{% extends 'base.html' %}

{% block content %}
<div class="row">
    <div class="col-lg-8 col-md-12">
        {% for property in properties %}
        <div class="property-box">
            <div class="property-thumbnail">
                <a href="{% url 'property_detail' property.id %}">
                    <img src="{{ property.photo.url }}" alt="{{ property.title }}">
                </a>
            </div>
            <div class="detail">
                <h4 class="property-title"><a href="{% url 'property_detail' property.id %}">{{ property.title }}</a></h4>
                <div class="location">{{ property.city }}, {{ property.state }}</div>
                <div class="price">{{ property.price|intcomma }} {{ property.currency }}</div>
            </div>
        </div>
        {% endfor %}
    </div>
    <div class="col-lg-4 col-md-12">
        <div class="sidebar mbl">
            <!-- Search box start -->
            <div class="widget search-box">
                <h5 class="sidebar-title">Search</h5>
                <form class="form-search" method="GET">
                    <input type="text" class="form-control" placeholder="Search">
                    <button type="submit" class="btn"><i class="fa fa-search"></i></button>
                </form>
            </div>
            <!-- Categories start -->
            <div class="widget categories">
                <h5 class="sidebar-title">Categories</h5>
                <ul>
                    {% for category in categories %}
                    <li><a href="#">{{ category.name }}<span>({{ category.property_count }})</span></a></li>
                    {% endfor %}
                </ul>
            </div>
            <!-- Recent posts start -->
            <div class="widget recent-posts">
                <h5 class="sidebar-title">Recent Properties</h5>
                {% for property in recent_properties %}
                <div class="media mb-4">
                    <a href="{% url 'property_detail' property.id %}">
                        <img src="{{ property.photo.url }}" alt="{{ property.title }}">
                    </a>
                    <div class="media-body align-self-center">
                        <h5><a href="{% url 'property_detail' property.id %}">{{ property.title }}</a></h5>
                        <p>{{ property.pub_date|date:"F j, Y" }} | {{ property.price|intcomma }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
            <!-- Tags start -->
            <div class="widget tags clearfix">
                <h5 class="sidebar-title">Tags</h5>
                <ul class="tags">
                    {% for tag in tags %}
                    <li><a href="#">{{ tag.name }}</a></li>
                    {% endfor %}
                </ul>
            </div>
            <!-- Recent comments start -->
            <div class="widget recent-comments">
                <h5 class="sidebar-title">Recent comments</h5>
                {% for comment in recent_comments %}
                <div class="media mb-4">
                    <a href="#">
                        <img src="{{ comment.user.profile_picture.url }}" alt="{{ comment.user.username }}">
                    </a>
                    <div class="media-body">
                        <h5>{{ comment.user.username }}</h5>
                        <p>{{ comment.text }}</p>
                    </div>
                </div>
                {% endfor %}
            </div>
            <!-- Latest start -->
            <div class="widget-3 latest-tweet">
                <h5 class="sidebar-title">Latest
